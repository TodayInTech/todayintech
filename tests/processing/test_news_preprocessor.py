from datetime import UTC, datetime

from src.models import Article, ServiceCollectionResult
from src.processing.briefed_article_store import BriefedArticleStore
from src.processing.news_preprocessor import NewsPreprocessor


def make_article(
    title: str,
    url: str,
    *,
    metadata: dict[str, str | int | float | bool] | None = None,
) -> Article:
    return Article(
        source="Hacker News",
        title=title,
        url=url,
        published_at=datetime(2026, 6, 10, tzinfo=UTC),
        collected_at=datetime(2026, 6, 11, tzinfo=UTC),
        summary="Agent release",
        metadata=metadata or {},
    )


def make_result(articles: list[Article]) -> ServiceCollectionResult:
    return ServiceCollectionResult(
        service_key="hacker-news",
        service_name="Hacker News",
        source_url="https://hnrss.org/frontpage",
        collection_method="rss",
        collected_at=datetime(2026, 6, 11, tzinfo=UTC),
        status="success",
        duration_ms=10,
        articles=articles,
    )


def test_news_preprocessor_deduplicates_and_filters_briefed_articles(tmp_path) -> None:
    store = BriefedArticleStore(tmp_path / "briefed_articles.json")
    store.mark_published(
        normalized_url="https://example.com/already-briefed",
        title_fingerprint="already briefed",
        service_key="hacker-news",
        title="Already Briefed",
        article_doc_path="docs/services/hacker-news/already-briefed.md",
        candidate_score=30,
    )

    preprocessor = NewsPreprocessor.create_default(
        briefed_article_store=store,
        per_service_limit=10,
        total_limit=10,
    )

    result = preprocessor.process(
        "2026-06-11",
        [
            make_result(
                [
                    make_article(
                        "New Agent Release",
                        "https://example.com/new-agent?utm_source=hn",
                        metadata={"hn_points": 120, "hn_comments": 40, "rss_rank": 1},
                    ),
                    make_article(
                        "New Agent Release",
                        "https://example.com/new-agent?utm_source=other",
                    ),
                    make_article(
                        "Already Briefed",
                        "https://example.com/already-briefed",
                    ),
                ]
            )
        ],
    )

    service = result.services[0]

    assert result.raw_count == 3
    assert service.candidate_count == 1
    assert service.excluded_count == 2
    assert service.candidates[0].normalized_url == "https://example.com/new-agent"
    assert service.candidates[0].candidate_id.startswith("hacker-news:")
    assert len(service.candidates[0].url_hash) == 64
    assert service.candidates[0].suggested_doc_key.startswith("2026-06-new-agent-release")
    assert service.candidates[0].suggested_article_path.startswith("docs/services/hacker-news/")
    assert service.candidates[0].feed_summary == "Agent release"
    assert service.candidates[0].candidate_score > 0
    assert result.archived_articles[0].title == "Already Briefed"
    assert result.archived_articles[0].candidate_score == 30
    assert {item.excluded_reason for item in service.excluded} == {
        "already_briefed",
        "duplicate_in_run",
    }


def test_news_preprocessor_applies_candidate_limits(tmp_path) -> None:
    preprocessor = NewsPreprocessor.create_default(
        briefed_article_store=BriefedArticleStore(tmp_path / "briefed_articles.json"),
        per_service_limit=1,
        total_limit=1,
    )

    result = preprocessor.process(
        "2026-06-11",
        [
            make_result(
                [
                    make_article("First Agent Release", "https://example.com/first"),
                    make_article("Second Agent Release", "https://example.com/second"),
                ]
            )
        ],
    )

    service = result.services[0]

    assert service.candidate_count == 1
    assert service.excluded_count == 1
    assert service.excluded[0].excluded_reason == "service_candidate_limit"
