from datetime import UTC, datetime, timedelta

from src.enrichment.models import (
    EnrichedArticleCandidate,
    EnrichmentFailureReason,
    EnrichmentInputStrategy,
    EnrichmentResult,
    EnrichmentStatus,
)
from src.enrichment.recovery import EvidenceRecoveryQueue
from src.models import Article
from src.processing.models import ArticleCandidate

NOW = datetime(2026, 10, 29, tzinfo=UTC)


def make_result(count=1, status=EnrichmentStatus.FALLBACK):
    return EnrichmentResult(
        generated_for="2026-10-29",
        generated_at=NOW,
        candidates=[
            EnrichedArticleCandidate(
                candidate=ArticleCandidate(
                    candidate_id=f"service:{i}",
                    service_key="service",
                    service_name="Service",
                    normalized_url=f"https://example.com/{i}",
                    article=Article(
                        source="Service",
                        title=f"Article {i}",
                        url=f"https://example.com/{i}",
                        collected_at=NOW,
                    ),
                ),
                status=status,
                input_strategy=EnrichmentInputStrategy.FULL_CONTENT
                if status == EnrichmentStatus.ENRICHED
                else EnrichmentInputStrategy.FEED_METADATA_ONLY,
                failure_reason=None
                if status == EnrichmentStatus.ENRICHED
                else EnrichmentFailureReason.ACCESS_DENIED,
            )
            for i in range(count)
        ],
    )


class Enricher:
    def __init__(self, status):
        self.status = status
        self.calls = []

    def enrich(self, preprocessing):
        self.calls.extend(
            candidate for service in preprocessing.services for candidate in service.candidates
        )
        result = make_result(status=self.status)
        result.candidates = [
            result.candidates[0].model_copy(update={"candidate": candidate})
            for candidate in self.calls
        ]
        return result


def test_queue_survives_restart_and_bounds_daily_rechecks(tmp_path):
    path = tmp_path / "requests.json"
    queue = EvidenceRecoveryQueue(path)
    queue.observe(make_result(8), now=NOW)
    queue.save()
    queue = EvidenceRecoveryQueue(path)
    enricher = Enricher(EnrichmentStatus.ENRICHED)
    assert queue.retry(enricher, generated_for="2026-10-29", now=NOW) is None
    result = queue.retry(
        enricher,
        generated_for="2026-10-30",
        now=NOW + timedelta(days=1),
        exclude_urls={"https://example.com/0"},
    )
    assert len(result.candidates) == 5
    assert len(enricher.calls) == 5
    assert queue.requests["https://example.com/0"].status == "pending"
    assert sum(item.status == "ready" for item in queue.requests.values()) == 5
    queue.save()
    # Persistent queue has only metadata, not extracted original content.
    assert "plain_text" not in path.read_text()


def test_persistent_failure_stops_after_seven_attempts(tmp_path):
    queue = EvidenceRecoveryQueue(tmp_path / "requests.json")
    queue.observe(make_result(), now=NOW)
    for attempt in range(7):
        queue.retry(
            Enricher(EnrichmentStatus.FALLBACK),
            generated_for="2026-10-30",
            now=NOW + timedelta(days=(attempt + 1) * 8),
        )
    request = queue.requests["https://example.com/0"]
    assert request.status == "exhausted"
    assert request.attempts == 7
    assert (
        queue.retry(
            Enricher(EnrichmentStatus.ENRICHED),
            generated_for="2026-12-30",
            now=NOW + timedelta(days=100),
        )
        is None
    )


def test_recovered_published_and_existing_files_never_return_to_writer(tmp_path):
    from src.enrichment.recovery import merge_unbriefed_recovery
    from src.processing.state.briefed_article_store import BriefedArticleStore

    recovered = make_result(3, EnrichmentStatus.ENRICHED)
    store = BriefedArticleStore(tmp_path / "briefed.json")
    store.mark_published(
        normalized_url="https://example.com/0",
        title_fingerprint="published",
        service_key="service",
        title="Published",
    )
    existing = tmp_path / "existing.md"
    existing.write_text("Already generated article")
    recovered.candidates[1].candidate.suggested_article_path = str(existing)
    current = make_result(0)
    merge_unbriefed_recovery(current, recovered, store)
    assert [item.candidate.normalized_url for item in current.candidates] == [
        "https://example.com/2"
    ]
    assert existing.read_text() == "Already generated article"


def test_ready_published_evidence_does_not_trigger_more_fetches(tmp_path):
    queue = EvidenceRecoveryQueue(tmp_path / "requests.json")
    queue.observe(make_result(), now=NOW)
    queue.observe(make_result(status=EnrichmentStatus.ENRICHED), now=NOW)
    enricher = Enricher(EnrichmentStatus.ENRICHED)
    assert (
        queue.retry(
            enricher,
            generated_for="2026-11-10",
            now=NOW + timedelta(days=10),
            briefed_urls={"https://example.com/0"},
        )
        is None
    )
    assert not enricher.calls


def test_writer_rejection_is_acknowledged_without_endless_regeneration(tmp_path):
    from types import SimpleNamespace

    from src.writer.agent.schemas import AgentDecisionStatus

    queue = EvidenceRecoveryQueue(tmp_path / "requests.json")
    queue.observe(make_result(), now=NOW)
    queue.observe(make_result(status=EnrichmentStatus.ENRICHED), now=NOW)
    queue.acknowledge(
        [
            SimpleNamespace(
                normalized_url="https://example.com/0", status=AgentDecisionStatus.SKIPPED
            )
        ]
    )
    assert queue.requests["https://example.com/0"].status == "reviewed"
    assert (
        queue.retry(
            Enricher(EnrichmentStatus.ENRICHED),
            generated_for="2026-11-10",
            now=NOW + timedelta(days=10),
        )
        is None
    )
