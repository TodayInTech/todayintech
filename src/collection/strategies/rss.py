import re
from datetime import UTC, datetime, timedelta
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
        config = source.source_config()
        collection_limit = config.get("collection_limit")
        lookback_days = config.get("lookback_days")
        articles: list[Article] = []

        for index, entry in enumerate(parsed.entries, start=1):
            article = self.normalize_entry(source, entry, collected_at, index)
            if article is not None:
                if self.is_older_than_lookback(article, collected_at, lookback_days):
                    continue
                articles.append(article)
            if collection_limit is not None and len(articles) >= collection_limit:
                break

        return articles

    def normalize_entry(
        self,
        source: BaseNewsSource,
        entry: Any,
        collected_at: datetime,
        rank: int,
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
        summary = getattr(entry, "summary", None)

        return Article(
            source=source.service_name,
            title=title.strip(),
            url=HttpUrl(link),
            published_at=published_at,
            collected_at=collected_at,
            summary=summary,
            authors=authors,
            tags=tags,
            metadata=self.build_metadata(source, summary, rank),
        )

    def is_older_than_lookback(
        self,
        article: Article,
        collected_at: datetime,
        lookback_days: int | None,
    ) -> bool:
        if lookback_days is None or article.published_at is None:
            return False
        return article.published_at < collected_at - timedelta(days=lookback_days)

    def build_metadata(
        self,
        source: BaseNewsSource,
        summary: str | None,
        rank: int,
    ) -> dict[str, str | int | float | bool]:
        metadata: dict[str, str | int | float | bool] = {
            "rss_rank": rank,
        }
        if source.service_key == "hacker-news":
            metadata.update(self.parse_hacker_news_metadata(summary))
        return metadata

    def parse_hacker_news_metadata(
        self,
        summary: str | None,
    ) -> dict[str, str | int | float | bool]:
        if not summary:
            return {}

        metadata: dict[str, str | int | float | bool] = {}
        points_match = re.search(r"Points:\s*(\d+)", summary, flags=re.IGNORECASE)
        comments_match = re.search(r"#\s*Comments:\s*(\d+)", summary, flags=re.IGNORECASE)
        comments_url_match = re.search(
            r"Comments URL:\s*<a href=\"([^\"]+)\"",
            summary,
            flags=re.IGNORECASE,
        )

        if points_match:
            metadata["hn_points"] = int(points_match.group(1))
        if comments_match:
            metadata["hn_comments"] = int(comments_match.group(1))
        if comments_url_match:
            metadata["hn_comments_url"] = comments_url_match.group(1)

        return metadata
