from datetime import UTC, datetime, timedelta
from types import SimpleNamespace

from src.collection.strategies.rss import RssCollector
from src.models import Article
from src.sources.implementations.hacker_news import HackerNewsSource


def test_rss_collector_filters_articles_older_than_lookback() -> None:
    collector = RssCollector()
    collected_at = datetime(2026, 6, 11, tzinfo=UTC)
    article = Article(
        source="Example",
        title="Old article",
        url="https://example.com/old",
        published_at=collected_at - timedelta(days=91),
        collected_at=collected_at,
    )

    assert collector.is_older_than_lookback(article, collected_at, 90) is True


def test_rss_collector_parses_hacker_news_metadata() -> None:
    collector = RssCollector()
    source = HackerNewsSource()
    entry = SimpleNamespace(
        title="Example HN story",
        link="https://example.com/story",
        published="Thu, 11 Jun 2026 01:00:00 GMT",
        summary=(
            '<p>Article URL: <a href="https://example.com/story">https://example.com/story</a></p>'
            '<p>Comments URL: <a href="https://news.ycombinator.com/item?id=1">'
            "https://news.ycombinator.com/item?id=1</a></p>"
            "<p>Points: 42</p>"
            "<p># Comments: 7</p>"
        ),
        authors=[],
        tags=[],
    )

    article = collector.normalize_entry(
        source,
        entry,
        datetime(2026, 6, 11, tzinfo=UTC),
        rank=3,
    )

    assert article is not None
    assert article.metadata["rss_rank"] == 3
    assert article.metadata["hn_points"] == 42
    assert article.metadata["hn_comments"] == 7
    assert article.metadata["hn_comments_url"] == "https://news.ycombinator.com/item?id=1"
