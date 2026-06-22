from collections import defaultdict
from datetime import UTC, datetime
from time import perf_counter

from src.models import ServiceCollectionResult
from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.enums import ExcludedReason
from src.processing.factories import PreprocessingPipelineFactory
from src.processing.models import (
    ArchivedArticle,
    ArticleCandidate,
    PreprocessingResult,
    PreprocessingStepMetrics,
    ServicePreprocessingResult,
)
from src.processing.state import BriefedArticleStore
from src.progress import log_info


class NewsPreprocessor:
    """Normalize raw collection results into Writer-facing article candidates."""

    def __init__(
        self,
        steps: list[BasePreprocessingStep],
        briefed_article_store: BriefedArticleStore,
    ) -> None:
        self.steps = steps
        self.briefed_article_store = briefed_article_store

    @classmethod
    def create_default(
        cls,
        *,
        briefed_article_store: BriefedArticleStore,
        per_service_limit: int,
        total_limit: int,
    ) -> NewsPreprocessor:
        pipeline_factory = PreprocessingPipelineFactory()
        return cls(
            steps=pipeline_factory.create_default(
                briefed_article_store=briefed_article_store,
                per_service_limit=per_service_limit,
                total_limit=total_limit,
            ),
            briefed_article_store=briefed_article_store,
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
            step_started_at = perf_counter()
            input_count = len(context.candidates)
            excluded_count_before = len(context.excluded)
            reason_counts_before = _excluded_reason_stats(context)
            context = step.process(context)
            context.add_step_metrics(
                PreprocessingStepMetrics(
                    step_name=step.name,
                    input_count=input_count,
                    output_count=len(context.candidates),
                    excluded_count=len(context.excluded) - excluded_count_before,
                    duration_ms=round((perf_counter() - step_started_at) * 1000),
                    reason_counts=_reason_count_delta(
                        before=reason_counts_before,
                        after=_excluded_reason_stats(context),
                    ),
                )
            )
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
            step_metrics=context.step_metrics,
            services=services,
            archived_articles=self.build_archived_articles(context),
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
        candidates_by_service = _group_by_service_key(context.candidates)
        excluded_by_service = _group_by_service_key(context.excluded)

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

    def build_archived_articles(self, context: PreprocessingContext) -> list[ArchivedArticle]:
        service_names = {
            result.service_key: result.service_name for result in context.collection_results
        }
        return [
            ArchivedArticle(
                service_key=record.service_key,
                service_name=service_names.get(record.service_key, record.service_key),
                title=record.title,
                article_doc_path=record.article_doc_path or "",
                status=record.status,
                briefed_at=record.briefed_at,
                candidate_score=record.candidate_score,
            )
            for record in sorted(
                self.briefed_article_store.active_records(),
                key=lambda item: (
                    item.candidate_score,
                    item.briefed_at.isoformat() if item.briefed_at else "",
                ),
                reverse=True,
            )
            if record.article_doc_path
        ]


def _group_by_service_key(
    items: list[ArticleCandidate],
) -> dict[str, list[ArticleCandidate]]:
    grouped: dict[str, list[ArticleCandidate]] = defaultdict(list)
    for item in items:
        grouped[item.service_key].append(item)
    return grouped


def _excluded_reason_stats(context: PreprocessingContext) -> dict[ExcludedReason, int]:
    counts: dict[ExcludedReason, int] = defaultdict(int)
    for candidate in context.excluded:
        if candidate.excluded_reason:
            counts[candidate.excluded_reason] += 1

    invalid_count = context.stats.get(f"excluded_reason:{ExcludedReason.INVALID_ARTICLE}", 0)
    if invalid_count:
        counts[ExcludedReason.INVALID_ARTICLE] += invalid_count
    return counts


def _reason_count_delta(
    *,
    before: dict[ExcludedReason, int],
    after: dict[ExcludedReason, int],
) -> dict[ExcludedReason, int]:
    return {
        reason: after_count - before.get(reason, 0)
        for reason, after_count in after.items()
        if after_count - before.get(reason, 0) > 0
    }
