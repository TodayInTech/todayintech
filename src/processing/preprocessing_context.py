from pydantic import BaseModel, Field

from src.models import ServiceCollectionResult
from src.processing.article_candidate import ArticleCandidate


class PreprocessingContext(BaseModel):
    generated_for: str
    collection_results: list[ServiceCollectionResult]
    candidates: list[ArticleCandidate] = Field(default_factory=list)
    excluded: list[ArticleCandidate] = Field(default_factory=list)
    stats: dict[str, int] = Field(default_factory=dict)
