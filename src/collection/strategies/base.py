from abc import ABC, abstractmethod
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime

from src.models import Article
from src.sources.contracts.base import BaseNewsSource


class BaseCollectorStrategy(ABC):
    collector_type: str

    @abstractmethod
    def collect(self, source: BaseNewsSource) -> list[Article]:
        """Collect articles for the given source metadata."""

    def parse_published_at(self, value: str | None) -> datetime | None:
        if not value:
            return None
        try:
            parsed = parsedate_to_datetime(value)
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)
        except TypeError, ValueError, IndexError, OverflowError:
            return None

    def parse_iso_datetime(self, value: str | None) -> datetime | None:
        if not value:
            return None
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)
        except ValueError:
            return None
