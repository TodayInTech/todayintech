from datetime import UTC, datetime

from src.models import Article
from src.processing.article_candidate import (
    ArticleCandidate,
    PreprocessingResult,
    ServicePreprocessingResult,
)
from src.tracing.preprocessing_trace import build_preprocessing_trace, write_preprocessing_trace


def make_candidate(excluded_reason: str | None = None) -> ArticleCandidate:
    return ArticleCandidate(
        candidate_id="openai-blog:abc123",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        article=Article(
            source="OpenAI Blog",
            title="New Agent Feature",
            url="https://openai.com/news/agent",
            published_at=datetime(2026, 6, 10, tzinfo=UTC),
            collected_at=datetime(2026, 6, 11, tzinfo=UTC),
        ),
        normalized_url="https://openai.com/news/agent",
        url_hash="abc123",
        title_fingerprint="new agent feature",
        suggested_doc_key="2026-06-new-agent-feature-abc123",
        suggested_article_path="docs/services/openai-blog/2026-06-new-agent-feature-abc123.md",
        candidate_score=42,
        excluded_reason=excluded_reason,
    )


def make_result() -> PreprocessingResult:
    return PreprocessingResult(
        generated_for="2026-06-11",
        generated_at=datetime(2026, 6, 11, tzinfo=UTC),
        duration_ms=15,
        raw_count=2,
        candidate_count=1,
        excluded_count=1,
        services=[
            ServicePreprocessingResult(
                service_key="openai-blog",
                service_name="OpenAI Blog",
                raw_count=2,
                candidate_count=1,
                excluded_count=1,
                candidates=[make_candidate()],
                excluded=[make_candidate("already_briefed")],
            )
        ],
    )


def test_build_preprocessing_trace_counts_excluded_reasons() -> None:
    trace = build_preprocessing_trace(make_result())

    assert trace["stage"] == "preprocessing"
    assert trace["duration_ms"] == 15
    assert trace["candidate_count"] == 1
    assert trace["excluded_count"] == 1
    assert trace["services"][0]["excluded_reasons"] == {"already_briefed": 1}
    assert trace["services"][0]["top_candidates"][0]["candidate_id"] == "openai-blog:abc123"
    assert trace["services"][0]["top_candidates"][0]["suggested_doc_key"] == (
        "2026-06-new-agent-feature-abc123"
    )


def test_write_preprocessing_trace_outputs_json_and_markdown(tmp_path) -> None:
    written_paths = write_preprocessing_trace(tmp_path, make_result())

    assert tmp_path.joinpath("2026-06-11", "preprocessing.json") in written_paths
    assert tmp_path.joinpath("2026-06-11", "preprocessing-summary.md") in written_paths
    assert tmp_path.joinpath("2026-06-11", "preprocessing.json").exists()
    assert tmp_path.joinpath("2026-06-11", "preprocessing-summary.md").exists()
