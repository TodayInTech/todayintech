from datetime import UTC, datetime

from src.models import Article
from src.processing.article_candidate import (
    ArticleCandidate,
    PreprocessingResult,
    ServicePreprocessingResult,
)
from src.processing.briefed_article_store import BriefedArticleStore
from src.writer import DraftNewsEditorAgent, NewsWriter
from src.writer.agent.schemas import EditorialStatus, GenerationMethod


def make_preprocessing_result() -> PreprocessingResult:
    article = Article(
        source="Hacker News",
        title="New Agent Feature",
        url="https://example.com/agent",
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
                service_key="hacker-news",
                service_name="Hacker News",
                raw_count=1,
                candidate_count=1,
                excluded_count=0,
                candidates=[
                    ArticleCandidate(
                        candidate_id="hacker-news:abc123",
                        service_key="hacker-news",
                        service_name="Hacker News",
                        article=article,
                        normalized_url="https://example.com/agent",
                        url_hash="abc123",
                        title_fingerprint="new agent feature",
                        feed_summary="Feed summary",
                        suggested_doc_key="2026-06-new-agent-feature-abc123",
                        suggested_article_path=(
                            "docs/articles/hacker-news/2026-06-new-agent-feature-abc123.md"
                        ),
                        candidate_score=42,
                        ranking_signals={"source_priority": 5},
                    )
                ],
            )
        ],
    )


def test_news_writer_writes_articles_indexes_and_draft_state(tmp_path) -> None:
    store = BriefedArticleStore(tmp_path / "briefed_articles.json")
    writer = NewsWriter(
        agent=DraftNewsEditorAgent(),
        output_dir=tmp_path / "docs",
        briefed_article_store=store,
    )

    result = writer.write(make_preprocessing_result())

    article_path = tmp_path.joinpath(
        "docs",
        "articles",
        "hacker-news",
        "2026-06-new-agent-feature-abc123.md",
    )
    service_path = tmp_path.joinpath("docs", "services", "hacker-news.md")
    index_path = tmp_path.joinpath("docs", "index.md")

    assert article_path in result.written_paths
    assert service_path in result.written_paths
    assert index_path in result.written_paths
    assert article_path.exists()
    assert service_path.exists()
    assert index_path.exists()
    article_content = article_path.read_text(encoding="utf-8")
    assert "> Hacker News · 2026-06-10 · draft" in article_content
    assert "아직 News Editor Agent가 브리핑 본문을 작성하지 않았습니다." in article_content
    assert "## 후보 판단 근거" in article_content

    reloaded = BriefedArticleStore(tmp_path / "briefed_articles.json")
    record = reloaded.state.articles[BriefedArticleStore.key_for_url("https://example.com/agent")]
    assert record.status == "draft"
    assert record.article_doc_path == (
        "docs/articles/hacker-news/2026-06-new-agent-feature-abc123.md"
    )


def test_news_writer_records_published_state_for_llm_briefing(tmp_path) -> None:
    preprocessing_result = make_preprocessing_result()
    briefing = DraftNewsEditorAgent().edit(preprocessing_result).services[0].briefings[0]
    briefing.editorial_status = EditorialStatus.PUBLISHED
    briefing.generation_method = GenerationMethod.LLM
    briefing.category = "AI"
    briefing.briefing_body_ko = "피드 기준으로 개발자 업데이트를 다룬 글입니다."

    class PublishedAgent:
        def edit(self, _preprocessing_result):
            result = DraftNewsEditorAgent().edit(_preprocessing_result)
            result.services[0].briefings = [briefing]
            return result

    writer = NewsWriter(
        agent=PublishedAgent(),
        output_dir=tmp_path / "docs",
        briefed_article_store=BriefedArticleStore(tmp_path / "briefed_articles.json"),
    )

    writer.write(preprocessing_result)

    reloaded = BriefedArticleStore(tmp_path / "briefed_articles.json")
    record = reloaded.state.articles[BriefedArticleStore.key_for_url("https://example.com/agent")]
    assert record.status == "published"
