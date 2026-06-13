from typing import Protocol

from src.processing.article_candidate import PreprocessingResult
from src.writer.agent.schemas import EditorialResult


class NewsEditorAgent(Protocol):
    def edit(self, preprocessing_result: PreprocessingResult) -> EditorialResult:
        """Create an editorial result from preprocessed candidates."""
        ...
