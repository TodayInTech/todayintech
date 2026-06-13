from collections import defaultdict
from datetime import UTC, datetime
from time import perf_counter

from src.models import ServiceCollectionResult
from src.processing.article_candidate import (
    ArticleCandidate,
    PreprocessingResult,
    ServicePreprocessingResult,
)
from src.processing.briefed_article_store import BriefedArticleStore
from src.processing.candidate_identity import (
    candidate_id,
    suggested_article_path,
    suggested_doc_key,
    url_hash,
)
from src.processing.candidate_scorer import DefaultCandidateScorer
from src.processing.preprocessing_context import PreprocessingContext
from src.processing.preprocessing_step import PreprocessingStep
from src.processing.url_normalizer import normalize_url, title_fingerprint
from src.progress import log_info


class ValidationStep:
    name = "validation"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        raw_count = 0
        for result in context.collection_results:
            raw_count += len(result.articles)
            if result.status == "failed":
                continue
            for article in result.articles:
                if not article.title.strip() or not str(article.url).strip():
                    context.stats["invalid_removed"] = context.stats.get("invalid_removed", 0) + 1
                    continue
                context.candidates.append(
                    ArticleCandidate(
                        service_key=result.service_key,
                        service_name=result.service_name,
                        article=article,
                    )
                )
        context.stats["raw_count"] = raw_count
        return context


class UrlNormalizationStep:
    name = "url_normalization"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        context.candidates = [
            candidate.model_copy(
                update={
                    "normalized_url": normalize_url(str(candidate.article.url)),
                    "title_fingerprint": title_fingerprint(candidate.article.title),
                }
            )
            for candidate in context.candidates
        ]
        return context


class CandidateIdentityStep:
    name = "candidate_identity"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        updated_candidates: list[ArticleCandidate] = []
        for candidate in context.candidates:
            candidate_url_hash = url_hash(candidate.normalized_url)
            doc_key = suggested_doc_key(candidate.article, candidate.normalized_url)
            updated_candidates.append(
                candidate.model_copy(
                    update={
                        "candidate_id": candidate_id(
                            candidate.service_key,
                            candidate.normalized_url,
                        ),
                        "url_hash": candidate_url_hash,
                        "feed_summary": candidate.article.summary or "",
                        "suggested_doc_key": doc_key,
                        "suggested_article_path": suggested_article_path(
                            candidate.service_key,
                            doc_key,
                        ),
                    }
                )
            )

        context.candidates = updated_candidates
        return context


class RunDeduplicationStep:
    name = "run_deduplication"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        seen_urls: set[str] = set()
        seen_titles: set[tuple[str, str]] = set()
        kept: list[ArticleCandidate] = []

        for candidate in context.candidates:
            title_key = (candidate.service_key, candidate.title_fingerprint)
            if candidate.normalized_url in seen_urls or title_key in seen_titles:
                context.excluded.append(
                    candidate.model_copy(update={"excluded_reason": "duplicate_in_run"})
                )
                context.stats["duplicate_removed"] = context.stats.get("duplicate_removed", 0) + 1
                continue
            seen_urls.add(candidate.normalized_url)
            seen_titles.add(title_key)
            kept.append(candidate)

        context.candidates = kept
        return context


class BriefedArticleFilterStep:
    name = "briefed_article_filter"

    def __init__(self, store: BriefedArticleStore) -> None:
        self.store = store

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        kept: list[ArticleCandidate] = []
        for candidate in context.candidates:
            if self.store.contains(
                candidate.normalized_url,
                candidate.title_fingerprint,
                candidate.service_key,
            ):
                context.excluded.append(
                    candidate.model_copy(update={"excluded_reason": "already_briefed"})
                )
                context.stats["already_briefed_removed"] = (
                    context.stats.get("already_briefed_removed", 0) + 1
                )
                continue
            kept.append(candidate)
        context.candidates = kept
        return context


class CandidateScoringStep:
    name = "candidate_scoring"

    def __init__(self, scorer: DefaultCandidateScorer | None = None) -> None:
        self.scorer = scorer or DefaultCandidateScorer()

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        context.candidates = [
            self.scorer.score(candidate)
            for candidate in sorted(
                context.candidates,
                key=lambda item: item.article.published_at or datetime.min.replace(tzinfo=UTC),
                reverse=True,
            )
        ]
        return context


class CandidateLimitStep:
    name = "candidate_limiting"

    def __init__(self, per_service_limit: int, total_limit: int) -> None:
        self.per_service_limit = per_service_limit
        self.total_limit = total_limit

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        by_service_count: dict[str, int] = defaultdict(int)
        kept: list[ArticleCandidate] = []

        for candidate in sorted(
            context.candidates,
            key=lambda item: item.candidate_score,
            reverse=True,
        ):
            if by_service_count[candidate.service_key] >= self.per_service_limit:
                context.excluded.append(
                    candidate.model_copy(update={"excluded_reason": "service_candidate_limit"})
                )
                context.stats["limit_removed"] = context.stats.get("limit_removed", 0) + 1
                continue
            if len(kept) >= self.total_limit:
                context.excluded.append(
                    candidate.model_copy(update={"excluded_reason": "total_candidate_limit"})
                )
                context.stats["limit_removed"] = context.stats.get("limit_removed", 0) + 1
                continue
            by_service_count[candidate.service_key] += 1
            kept.append(candidate)

        context.candidates = kept
        return context


class NewsPreprocessor:
    def __init__(self, steps: list[PreprocessingStep]) -> None:
        self.steps = steps

    @classmethod
    def create_default(
        cls,
        *,
        briefed_article_store: BriefedArticleStore,
        per_service_limit: int,
        total_limit: int,
    ) -> NewsPreprocessor:
        return cls(
            steps=[
                ValidationStep(),
                UrlNormalizationStep(),
                CandidateIdentityStep(),
                RunDeduplicationStep(),
                BriefedArticleFilterStep(briefed_article_store),
                CandidateScoringStep(),
                CandidateLimitStep(per_service_limit, total_limit),
            ]
        )

    def process(
        self,
        generated_for: str,
        collection_results: list[ServiceCollectionResult],
    ) -> PreprocessingResult:
        started_at = perf_counter()
        context = PreprocessingContext(
            generated_for=generated_for,
            collection_results=collection_results,
        )
        for index, step in enumerate(self.steps, start=1):
            log_info("Preprocessor", f"({index}/{len(self.steps)}) {step.name} 시작")
            context = step.process(context)
            log_info(
                "Preprocessor",
                (
                    f"({index}/{len(self.steps)}) {step.name} 완료: "
                    f"candidates={len(context.candidates)}, excluded={len(context.excluded)}"
                ),
            )

        services = self.build_service_results(context)
        return PreprocessingResult(
            generated_for=generated_for,
            generated_at=datetime.now(UTC),
            duration_ms=round((perf_counter() - started_at) * 1000),
            raw_count=context.stats.get("raw_count", 0),
            candidate_count=sum(service.candidate_count for service in services),
            excluded_count=sum(service.excluded_count for service in services),
            services=services,
        )

    def build_service_results(
        self,
        context: PreprocessingContext,
    ) -> list[ServicePreprocessingResult]:
        raw_counts = {
            result.service_key: len(result.articles) for result in context.collection_results
        }
        service_names = {
            result.service_key: result.service_name for result in context.collection_results
        }
        candidates_by_service: dict[str, list[ArticleCandidate]] = defaultdict(list)
        excluded_by_service: dict[str, list[ArticleCandidate]] = defaultdict(list)

        for candidate in context.candidates:
            candidates_by_service[candidate.service_key].append(candidate)
        for candidate in context.excluded:
            excluded_by_service[candidate.service_key].append(candidate)

        service_keys = sorted(
            set(raw_counts) | set(candidates_by_service) | set(excluded_by_service)
        )
        return [
            ServicePreprocessingResult(
                service_key=service_key,
                service_name=service_names.get(service_key, service_key),
                raw_count=raw_counts.get(service_key, 0),
                candidate_count=len(candidates_by_service.get(service_key, [])),
                excluded_count=len(excluded_by_service.get(service_key, [])),
                candidates=candidates_by_service.get(service_key, []),
                excluded=excluded_by_service.get(service_key, []),
            )
            for service_key in service_keys
        ]
