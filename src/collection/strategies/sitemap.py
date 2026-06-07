from datetime import UTC, datetime
from html.parser import HTMLParser
from urllib.parse import urlparse
from xml.etree import ElementTree

import httpx
from pydantic import HttpUrl

from src.collection.strategies.base import BaseCollectorStrategy
from src.models import Article
from src.sources.contracts.base import BaseNewsSource


class PageMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title = ""
        self.description: str | None = None
        self.og_title: str | None = None
        self.og_description: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key.lower(): value for key, value in attrs if value is not None}
        if tag.lower() == "title":
            self.in_title = True
            return
        if tag.lower() != "meta":
            return

        name = attr_map.get("name", "").lower()
        property_name = attr_map.get("property", "").lower()
        content = attr_map.get("content")
        if not content:
            return

        if name == "description":
            self.description = content
        elif property_name == "og:title":
            self.og_title = content
        elif property_name == "og:description":
            self.og_description = content

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


class SitemapCollector(BaseCollectorStrategy):
    collector_type = "sitemap"

    def collect(self, source: BaseNewsSource) -> list[Article]:
        config = source.source_config()
        url_prefixes = config.get("url_prefixes", ())
        collection_limit = config.get("collection_limit", 20)
        sitemap_entries = self.fetch_sitemap_entries(source.source_url, url_prefixes)
        collected_at = datetime.now(UTC)
        articles: list[Article] = []

        for url, lastmod in sitemap_entries[:collection_limit]:
            article = self.fetch_article_metadata(source, url, lastmod, collected_at)
            if article is not None:
                articles.append(article)

        return articles

    def fetch_sitemap_entries(
        self,
        sitemap_url: str,
        url_prefixes: tuple[str, ...],
    ) -> list[tuple[str, datetime | None]]:
        response = httpx.get(sitemap_url, timeout=20.0)
        response.raise_for_status()

        root = ElementTree.fromstring(response.content)
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        entries: list[tuple[str, datetime | None]] = []

        for url_element in root.findall("sm:url", namespace):
            loc = url_element.findtext("sm:loc", default="", namespaces=namespace)
            if not loc or not self.should_include_url(loc, url_prefixes):
                continue
            lastmod = self.parse_iso_datetime(
                url_element.findtext("sm:lastmod", default="", namespaces=namespace)
            )
            entries.append((loc, lastmod))

        return sorted(
            entries,
            key=lambda entry: entry[1] or datetime.min.replace(tzinfo=UTC),
            reverse=True,
        )

    def should_include_url(self, url: str, url_prefixes: tuple[str, ...]) -> bool:
        path = urlparse(url).path
        return any(
            path.startswith(prefix) and path != prefix.rstrip("/") for prefix in url_prefixes
        )

    def fetch_article_metadata(
        self,
        source: BaseNewsSource,
        url: str,
        lastmod: datetime | None,
        collected_at: datetime,
    ) -> Article | None:
        response = httpx.get(url, timeout=20.0)
        response.raise_for_status()

        parser = PageMetadataParser()
        parser.feed(response.text)

        title = (parser.og_title or parser.title).strip()
        if not title:
            return None

        return Article(
            source=source.service_name,
            title=title.replace("\\ Anthropic", "").strip(),
            url=HttpUrl(url),
            published_at=lastmod,
            collected_at=collected_at,
            summary=parser.og_description or parser.description,
            tags=[self.collector_type],
        )
