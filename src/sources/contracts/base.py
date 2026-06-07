from abc import ABC, abstractmethod

from src.sources.contracts.config import SourceConfig


class BaseNewsSource(ABC):
    """Base metadata contract for all news source integrations."""

    service_key: str
    service_name: str
    collector_type: str
    source_url: str

    @abstractmethod
    def source_config(self) -> SourceConfig:
        """Return collector-specific configuration."""
