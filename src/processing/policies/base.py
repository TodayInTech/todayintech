from abc import ABC, abstractmethod

from src.processing.models import ArticleCandidate


class BasePreprocessingPolicy(ABC):
    @abstractmethod
    def reject_reason(self, candidate: ArticleCandidate) -> str | None:
        """Return a Korean rejection reason when a candidate should be filtered."""
