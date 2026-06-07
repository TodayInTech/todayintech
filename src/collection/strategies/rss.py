from datetime import UTC, datetime
from typing import Any

import feedparser
from pydantic import HttpUrl

from src.collection.strategies.base import BaseCollectorStrategy
from src.models import Article
from src.sources.contracts.base import BaseNewsSource


class RssCollector(BaseCollectorStrategy):
    collector_type = "rss"

    def collect(self, source: BaseNewsSource) -> list[Article]:
        parsed = feedparser.parse(source.source_url)
        collected_at = datetime.now(UTC)
        articles: list[Article] = []

        for entry in parsed.entries:
            article = self.normalize_entry(source, entry, collected_at)
            if article is not None:
                articles.append(article)

        return articles

    def normalize_entry(
        self,
        source: BaseNewsSource,
        entry: Any,
        collected_at: datetime,
    ) -> Article | None:
        title = getattr(entry, "title", None)
        link = getattr(entry, "link", None)
        if not title or not link:
            return None

        published_at = self.parse_published_at(
            getattr(entry, "published", None) or getattr(entry, "updated", None)
        )
        authors = [
            author.name for author in getattr(entry, "authors", []) if hasattr(author, "name")
        ]
        tags = [tag.term for tag in getattr(entry, "tags", []) if hasattr(tag, "term")]

        return Article(
            source=source.service_name,
            title=title.strip(),
            url=HttpUrl(link),
            published_at=published_at,
            collected_at=collected_at,
            summary=getattr(entry, "summary", None),
            authors=authors,
            tags=tags,
        )
