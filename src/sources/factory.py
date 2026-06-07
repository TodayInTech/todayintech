from abc import ABC, abstractmethod

from src.sources.contracts.base import BaseNewsSource
from src.sources.implementations.anthropic_blog import AnthropicBlogSource
from src.sources.implementations.github_blog import GitHubBlogSource
from src.sources.implementations.google_blog import GoogleBlogSource
from src.sources.implementations.hacker_news import HackerNewsSource
from src.sources.implementations.openai_blog import OpenAIBlogSource


class AbstractNewsSourceFactory(ABC):
    @abstractmethod
    def create(self, service_key: str) -> BaseNewsSource:
        """Create a news source by service key."""

    @abstractmethod
    def create_all(self) -> list[BaseNewsSource]:
        """Create every registered news source."""

    @abstractmethod
    def service_keys(self) -> tuple[str, ...]:
        """Return every registered service key."""


class NewsSourceFactory(AbstractNewsSourceFactory):
    _registry: dict[str, type[BaseNewsSource]] = {
        HackerNewsSource.service_key: HackerNewsSource,
        GitHubBlogSource.service_key: GitHubBlogSource,
        GoogleBlogSource.service_key: GoogleBlogSource,
        OpenAIBlogSource.service_key: OpenAIBlogSource,
        AnthropicBlogSource.service_key: AnthropicBlogSource,
    }

    def create(self, service_key: str) -> BaseNewsSource:
        try:
            source_class = self._registry[service_key]
        except KeyError as exc:
            available = ", ".join(sorted(self._registry))
            raise ValueError(f"Unknown service '{service_key}'. Available: {available}") from exc
        return source_class()

    def create_all(self) -> list[BaseNewsSource]:
        return [source_class() for source_class in self._registry.values()]

    def service_keys(self) -> tuple[str, ...]:
        return tuple(self._registry)
