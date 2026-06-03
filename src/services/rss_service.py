from datetime import datetime
from typing import Any

from src.models import Article
from src.services.base import BaseNewsService


class RssNewsService(BaseNewsService):
    """Default RSS/Atom service implementation."""

    service_key: str
    service_name: str
    feed_url: str

    def normalize_entry(self, entry: Any, collected_at: datetime) -> Article | None:
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
            source=self.service_name,
            title=title.strip(),
            url=link,
            published_at=published_at,
            collected_at=collected_at,
            summary=getattr(entry, "summary", None),
            authors=authors,
            tags=tags,
        )
