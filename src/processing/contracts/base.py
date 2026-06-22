from abc import ABC, abstractmethod

from src.processing.context import PreprocessingContext


class BasePreprocessingStep(ABC):
    name: str

    @abstractmethod
    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        """Process and return preprocessing context."""
