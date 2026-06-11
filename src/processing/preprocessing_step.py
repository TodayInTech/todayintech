from typing import Protocol

from src.processing.preprocessing_context import PreprocessingContext


class PreprocessingStep(Protocol):
    name: str

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        """Process and return preprocessing context."""
        ...
