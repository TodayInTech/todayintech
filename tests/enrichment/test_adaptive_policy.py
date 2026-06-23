from datetime import UTC, datetime

from src.enrichment.context import EnrichmentContext
from src.enrichment.models import (
    EnrichmentInputStrategy,
    EnrichmentRecord,
    EnrichmentStatus,
    ExtractedDocument,
)
from src.enrichment.policies import AdaptiveEnrichmentPolicy
from src.models import Article
from src.processing.models import ArticleCandidate


def make_context(token_count: int) -> EnrichmentContext:
    candidate = ArticleCandidate(
        candidate_id="openai-blog:abc",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        normalized_url="https://openai.com/index/agent",
        article=Article(
            source="OpenAI Blog",
            title="Agent Architecture",
            url="https://openai.com/index/agent",
            collected_at=datetime(2026, 6, 23, tzinfo=UTC),
        ),
    )
    return EnrichmentContext(
        candidate=candidate,
        record=EnrichmentRecord(
            candidate_id=candidate.candidate_id,
            service_key=candidate.service_key,
            service_name=candidate.service_name,
            title=candidate.article.title,
            source_url=candidate.normalized_url,
            status=EnrichmentStatus.FAILED,
            input_strategy=EnrichmentInputStrategy.NONE,
        ),
        extracted_document=ExtractedDocument(
            plain_text="document",
            content_hash="abc",
            char_count=8,
            token_count=token_count,
        ),
    )


def test_adaptive_policy_routes_by_token_budget_without_selecting_evidence() -> None:
    policy = AdaptiveEnrichmentPolicy()

    assert policy.version == "1:min=100:full=4000:select=8000"
    assert policy.decide(make_context(4000)).input_strategy == (
        EnrichmentInputStrategy.FULL_CONTENT
    )
    medium = policy.decide(make_context(4001))
    assert medium.input_strategy == EnrichmentInputStrategy.CHUNK_SELECTION
    assert medium.selected_chunks == []
    large = policy.decide(make_context(8001))
    assert large.input_strategy == EnrichmentInputStrategy.EVIDENCE_SELECTION
    assert large.selected_chunks == []
