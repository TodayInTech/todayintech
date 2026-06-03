from abc import ABC, abstractmethod

from src.services.anthropic_blog import AnthropicBlogService
from src.services.base import BaseNewsService
from src.services.github_blog import GitHubBlogService
from src.services.google_blog import GoogleBlogService
from src.services.hacker_news import HackerNewsService
from src.services.openai_blog import OpenAIBlogService


class AbstractNewsServiceFactory(ABC):
    @abstractmethod
    def create(self, service_key: str) -> BaseNewsService:
        """Create a news service by service key."""

    @abstractmethod
    def create_all(self) -> list[BaseNewsService]:
        """Create every registered news service."""


class NewsServiceFactory(AbstractNewsServiceFactory):
    _registry: dict[str, type[BaseNewsService]] = {
        HackerNewsService.service_key: HackerNewsService,
        GitHubBlogService.service_key: GitHubBlogService,
        GoogleBlogService.service_key: GoogleBlogService,
        OpenAIBlogService.service_key: OpenAIBlogService,
        AnthropicBlogService.service_key: AnthropicBlogService,
    }

    def create(self, service_key: str) -> BaseNewsService:
        try:
            service_class = self._registry[service_key]
        except KeyError as exc:
            available = ", ".join(sorted(self._registry))
            raise ValueError(f"Unknown service '{service_key}'. Available: {available}") from exc
        return service_class()

    def create_all(self) -> list[BaseNewsService]:
        return [service_class() for service_class in self._registry.values()]
