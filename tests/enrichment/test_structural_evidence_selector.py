from datetime import UTC, datetime

from src.enrichment.context import EnrichmentContext
from src.enrichment.models import (
    EnrichmentInputStrategy,
    EnrichmentRecord,
    EnrichmentStatus,
    EvidenceChunk,
)
from src.enrichment.selectors import StructuralEvidenceSelector
from src.models import Article
from src.processing.models import ArticleCandidate


def make_context() -> EnrichmentContext:
    candidate = ArticleCandidate(
        candidate_id="openai-blog:agents",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        normalized_url="https://openai.com/index/agents",
        feed_summary="OpenAI explains agent reliability, evaluation, and developer workflow.",
        article=Article(
            source="OpenAI Blog",
            title="Improving agent reliability for developers",
            url="https://openai.com/index/agents",
            collected_at=datetime(2026, 6, 23, tzinfo=UTC),
            tags=["agents", "developers"],
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
        chunks=[
            EvidenceChunk(
                chunk_id="chunk-0001",
                heading_path=["Intro"],
                text="This post introduces the broader context.",
                block_ids=["block-0001"],
                token_count=20,
                position=0,
            ),
            EvidenceChunk(
                chunk_id="chunk-0002",
                heading_path=["Agent reliability"],
                text="Agent reliability improves when developers combine evaluation and workflow checks.",
                block_ids=["block-0002"],
                token_count=30,
                position=1,
            ),
            EvidenceChunk(
                chunk_id="chunk-0003",
                heading_path=["Pricing"],
                text="Billing and account administration details.",
                block_ids=["block-0003"],
                token_count=20,
                position=2,
            ),
            EvidenceChunk(
                chunk_id="chunk-0004",
                heading_path=["Conclusion"],
                text="The final section summarizes developer impact.",
                block_ids=["block-0004"],
                token_count=20,
                position=3,
            ),
        ],
    )


def test_structural_evidence_selector_prefers_relevant_chunks_with_boundaries() -> None:
    selector = StructuralEvidenceSelector(max_selected_tokens=70)

    selected = selector.select(make_context())

    assert [chunk.chunk_id for chunk in selected] == [
        "chunk-0001",
        "chunk-0002",
        "chunk-0004",
    ]
    assert sum(chunk.token_count for chunk in selected) <= 70
