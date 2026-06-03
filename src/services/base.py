from abc import ABC, abstractmethod
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any

import feedparser

from src.models import Article


class BaseNewsService(ABC):
    """Base interface for all news source integrations."""

    service_key: str
    service_name: str
    feed_url: str

    @abstractmethod
    def normalize_entry(self, entry: Any, collected_at: datetime) -> Article | None:
        """Convert a feed entry into the shared Article model."""

    def collect(self) -> list[Article]:
        parsed = feedparser.parse(self.feed_url)
        collected_at = datetime.now(UTC)
        articles: list[Article] = []

        for entry in parsed.entries:
            article = self.normalize_entry(entry, collected_at)
            if article is not None:
                articles.append(article)

        return articles

    def parse_published_at(self, value: str | None) -> datetime | None:
        if not value:
            return None
        try:
            parsed = parsedate_to_datetime(value)
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)
        except TypeError, ValueError, IndexError, OverflowError:
            return None
