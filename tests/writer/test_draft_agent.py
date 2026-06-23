from datetime import UTC, datetime

from src.enrichment.models import (
    EnrichedArticleCandidate,
    EnrichmentInputStrategy,
    EnrichmentResult,
    EnrichmentStatus,
)
from src.models import Article
from src.processing.models import (
    ArticleCandidate,
    PreprocessingResult,
    ServicePreprocessingResult,
)
from src.writer.agent.draft_agent import DraftNewsEditorAgent
from src.writer.agent.schemas import EditorialStatus, GenerationMethod


def make_preprocessing_result() -> PreprocessingResult:
    article = Article(
        source="OpenAI Blog",
        title="New Agent Feature",
        url="https://openai.com/news/agent",
        published_at=datetime(2026, 6, 10, tzinfo=UTC),
        collected_at=datetime(2026, 6, 11, tzinfo=UTC),
        summary="Feed summary",
    )
    return PreprocessingResult(
        generated_for="2026-06-11",
        generated_at=datetime(2026, 6, 11, tzinfo=UTC),
        raw_count=1,
        candidate_count=1,
        excluded_count=0,
        services=[
            ServicePreprocessingResult(
                service_key="openai-blog",
                service_name="OpenAI Blog",
                raw_count=1,
                candidate_count=1,
                excluded_count=0,
                candidates=[
                    ArticleCandidate(
                        candidate_id="openai-blog:abc123",
                        service_key="openai-blog",
                        service_name="OpenAI Blog",
                        article=article,
                        normalized_url="https://openai.com/news/agent",
                        url_hash="abc123",
                        title_fingerprint="new agent feature",
                        feed_summary="Feed summary",
                        suggested_doc_key="2026-06-new-agent-feature-abc123",
                        suggested_article_path=(
                            "docs/services/openai-blog/2026-06-new-agent-feature-abc123.md"
                        ),
                        candidate_score=42,
                        ranking_signals={"source_priority": 10},
                    )
                ],
            )
        ],
    )


def make_enrichment_result() -> EnrichmentResult:
    preprocessing = make_preprocessing_result()
    candidate = preprocessing.services[0].candidates[0]
    return EnrichmentResult(
        generated_for=preprocessing.generated_for,
        generated_at=preprocessing.generated_at,
        candidates=[
            EnrichedArticleCandidate(
                candidate=candidate,
                status=EnrichmentStatus.FALLBACK,
                input_strategy=EnrichmentInputStrategy.FEED_METADATA_ONLY,
            )
        ],
    )


def test_draft_agent_creates_draft_briefing_without_editorial_body() -> None:
    result = DraftNewsEditorAgent().edit(make_enrichment_result())
    briefing = result.services[0].briefings[0]

    assert briefing.editorial_status == EditorialStatus.DRAFT
    assert briefing.generation_method == GenerationMethod.DRAFT
    assert briefing.summary_ko is None
