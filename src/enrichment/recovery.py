"""Bounded source rechecks, independent of article generation and deduplication."""

import argparse
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel

from src.enrichment.models import EnrichmentResult, EnrichmentStatus
from src.processing.models import ArticleCandidate, PreprocessingResult, ServicePreprocessingResult
from src.processing.state.briefed_article_store import BriefedArticleStore

if TYPE_CHECKING:
    from src.enrichment.content_enricher import ContentEnricher
    from src.writer.agent.schemas import AgentDecision


class EvidenceRequest(BaseModel):
    candidate: ArticleCandidate
    status: Literal["pending", "ready", "exhausted", "reviewed"] = "pending"
    attempts: int = 0
    next_attempt_at: datetime
    last_failure: str | None = None
    recovered_at: datetime | None = None
    extraction_method: str | None = None
    token_count: int = 0


class EvidenceRecoveryQueue:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.requests: dict[str, EvidenceRequest] = {}
        if path.exists():
            self.requests = {
                key: EvidenceRequest.model_validate(value)
                for key, value in json.loads(path.read_text()).items()
            }

    def observe(self, result: EnrichmentResult, *, now: datetime | None = None) -> None:
        now = now or datetime.now(UTC)
        for item in result.candidates:
            key = item.candidate.normalized_url
            if item.status == EnrichmentStatus.ENRICHED:
                if key in self.requests:
                    request = self.requests[key]
                    request.status = "ready"
                    request.recovered_at = now
                    request.next_attempt_at = now
                    request.last_failure = None
                    request.extraction_method = (
                        item.document.extraction_method if item.document else None
                    )
                    request.token_count = item.document.token_count if item.document else 0
                continue
            if item.status not in {EnrichmentStatus.FAILED, EnrichmentStatus.FALLBACK}:
                continue
            if key not in self.requests:
                self.requests[key] = EvidenceRequest(
                    candidate=item.candidate,
                    next_attempt_at=now + timedelta(days=1),
                    last_failure=item.failure_reason.value if item.failure_reason else None,
                )

    def retry(
        self,
        enricher: ContentEnricher,
        *,
        generated_for: str,
        exclude_urls: set[str] | None = None,
        briefed_urls: set[str] | None = None,
        now: datetime | None = None,
        limit: int = 5,
    ) -> EnrichmentResult | None:
        now = now or datetime.now(UTC)
        excluded = exclude_urls or set()
        briefed = briefed_urls or set()
        due = sorted(
            (
                item
                for key, item in self.requests.items()
                if (item.status == "pending" or (item.status == "ready" and key not in briefed))
                and item.next_attempt_at <= now
                and key not in excluded
            ),
            key=lambda item: item.next_attempt_at,
        )[:limit]
        if not due:
            return None
        services = {}
        for request in due:
            candidate = request.candidate.model_copy(update={"excluded_reason": None})
            service = services.setdefault(
                candidate.service_key,
                ServicePreprocessingResult(
                    service_key=candidate.service_key,
                    service_name=candidate.service_name,
                    raw_count=0,
                    candidate_count=0,
                    excluded_count=0,
                ),
            )
            service.candidates.append(candidate)
            service.candidate_count += 1
            service.raw_count += 1
        result = enricher.enrich(
            PreprocessingResult(
                generated_for=generated_for,
                generated_at=now,
                raw_count=len(due),
                candidate_count=len(due),
                excluded_count=0,
                services=list(services.values()),
            )
        )
        self.observe(result, now=now)
        for item in result.candidates:
            request = self.requests[item.candidate.normalized_url]
            request.attempts += 1
            request.next_attempt_at = now + timedelta(days=min(2**request.attempts, 7))
            if item.status != EnrichmentStatus.ENRICHED:
                request.last_failure = item.failure_reason.value if item.failure_reason else None
                request.status = "exhausted" if request.attempts >= 7 else "pending"
        return result

    def acknowledge(self, decisions: list[AgentDecision]) -> None:
        for decision in decisions:
            request = self.requests.get(decision.normalized_url)
            if (
                request is not None
                and request.status == "ready"
                and decision.status.value in {"published", "draft", "skipped"}
            ):
                request.status = "reviewed"

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(
                {key: value.model_dump(mode="json") for key, value in self.requests.items()},
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )


def merge_unbriefed_recovery(
    current: EnrichmentResult, recovered: EnrichmentResult, store: BriefedArticleStore
) -> None:
    """Keep published/draft URLs and existing files out of the Writer, even after recovery."""
    existing_urls = {item.candidate.normalized_url for item in current.candidates}
    eligible_ids = set()
    for item in recovered.candidates:
        candidate = item.candidate
        if item.status != EnrichmentStatus.ENRICHED or candidate.normalized_url in existing_urls:
            continue
        if store.contains(
            candidate.normalized_url,
            candidate.title_fingerprint,
            candidate.service_key,
            candidate.suggested_article_path,
        ):
            continue
        current.candidates.append(item)
        existing_urls.add(candidate.normalized_url)
        eligible_ids.add(candidate.candidate_id)
    current.records.extend(
        record for record in recovered.records if record.candidate_id in eligible_ids
    )
    current.service_names.update(recovered.service_names)


def main() -> None:
    from src.enrichment.content_enricher import ContentEnricher
    from src.enrichment.storage import write_enrichment_result
    from src.settings import SETTINGS

    parser = argparse.ArgumentParser(
        description="Recheck original evidence without generating or overwriting articles."
    )
    parser.add_argument(
        "--seed", type=Path, help="Previous enrichment.json containing failed/feed-only candidates"
    )
    parser.add_argument(
        "--queue",
        type=Path,
        default=SETTINGS.briefed_articles_path.with_name("evidence_requests.json"),
    )
    parser.add_argument("--output-dir", type=Path, default=Path(".var/local/recovered"))
    parser.add_argument(
        "--retry-now",
        action="store_true",
        help="Make pending requests due now; exhausted requests stay exhausted",
    )
    args = parser.parse_args()
    queue = EvidenceRecoveryQueue(args.queue)
    if args.seed:
        queue.observe(EnrichmentResult.model_validate_json(args.seed.read_text()))
    if args.retry_now:
        for request in queue.requests.values():
            if request.status == "pending":
                request.next_attempt_at = datetime.now(UTC)
    enricher = ContentEnricher.create_default(
        cache_dir=SETTINGS.enrichment_cache_dir,
        timeout_seconds=SETTINGS.enrichment_timeout_seconds,
        max_attempts=SETTINGS.enrichment_max_attempts,
        minimum_tokens=SETTINGS.enrichment_minimum_tokens,
        full_content_max_tokens=SETTINGS.enrichment_full_content_max_tokens,
        chunk_selection_max_tokens=SETTINGS.enrichment_chunk_selection_max_tokens,
        chunk_max_tokens=SETTINGS.enrichment_chunk_max_tokens,
        selected_chunks_max_tokens=SETTINGS.enrichment_selected_chunks_max_tokens,
    )
    result = queue.retry(
        enricher,
        generated_for=SETTINGS.resolve_target_date(None),
        briefed_urls={key for key, request in queue.requests.items() if request.status == "ready"},
    )
    queue.save()
    if result:
        write_enrichment_result(args.output_dir / result.generated_for, result)
    counts = {
        status: sum(item.status == status for item in queue.requests.values())
        for status in ("pending", "ready", "exhausted")
    }
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
