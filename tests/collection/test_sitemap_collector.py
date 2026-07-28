from datetime import UTC, datetime
from types import SimpleNamespace

import httpx

from src.collection.strategies.sitemap import SitemapCollector
from src.sources.implementations.anthropic_blog import AnthropicBlogSource


def test_sitemap_collector_follows_article_redirects(monkeypatch) -> None:
    collector = SitemapCollector()
    source = AnthropicBlogSource()

    html = """
    <html>
      <head>
        <meta property="og:title" content="Skills \\ Anthropic">
        <meta property="og:description" content="Use skills with Claude.">
      </head>
    </html>
    """

    def fake_get(url: str, **kwargs):
        assert kwargs["follow_redirects"] is True
        return SimpleNamespace(
            text=html,
            url=httpx.URL("https://claude.com/blog/skills"),
            raise_for_status=lambda: None,
        )

    monkeypatch.setattr(httpx, "get", fake_get)

    article = collector.fetch_article_metadata(
        source,
        "https://www.anthropic.com/news/skills",
        datetime(2026, 7, 22, tzinfo=UTC),
        datetime(2026, 7, 28, tzinfo=UTC),
    )

    assert article is not None
    assert str(article.url) == "https://claude.com/blog/skills"


def test_sitemap_collector_skips_failed_article_metadata(monkeypatch) -> None:
    collector = SitemapCollector()
    source = AnthropicBlogSource()

    monkeypatch.setattr(
        collector,
        "fetch_sitemap_entries",
        lambda *_args: [
            ("https://www.anthropic.com/news/broken", datetime(2026, 7, 22, tzinfo=UTC)),
            ("https://www.anthropic.com/news/valid", datetime(2026, 7, 21, tzinfo=UTC)),
        ],
    )

    def fake_fetch_metadata(_source, url, lastmod, collected_at):
        if url.endswith("/broken"):
            raise httpx.HTTPStatusError(
                "boom",
                request=httpx.Request("GET", url),
                response=httpx.Response(500),
            )
        return SimpleNamespace(url=url, title="Valid")

    monkeypatch.setattr(collector, "fetch_article_metadata", fake_fetch_metadata)

    articles = collector.collect(source)

    assert len(articles) == 1
    assert collector.warning_codes == ["article_metadata_fetch_failed"]
