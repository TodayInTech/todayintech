from abc import ABC, abstractmethod

from src.processing.models import ArticleCandidate


class BaseCandidateScorer(ABC):
    @abstractmethod
    def score(self, candidate: ArticleCandidate) -> ArticleCandidate:
        """Return the candidate with score and ranking signals applied."""
