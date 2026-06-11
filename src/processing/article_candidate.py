from datetime import datetime

from pydantic import BaseModel, Field

from src.models import Article


class ArticleCandidate(BaseModel):
    service_key: str
    service_name: str
    article: Article
    normalized_url: str = ""
    title_fingerprint: str = ""
    candidate_score: float = 0
    ranking_signals: dict[str, str | int | float | bool] = Field(default_factory=dict)
    excluded_reason: str | None = None


class ServicePreprocessingResult(BaseModel):
    service_key: str
    service_name: str
    raw_count: int
    candidate_count: int
    excluded_count: int
    candidates: list[ArticleCandidate] = Field(default_factory=list)
    excluded: list[ArticleCandidate] = Field(default_factory=list)


class PreprocessingResult(BaseModel):
    generated_for: str
    generated_at: datetime
    duration_ms: int = Field(default=0, ge=0)
    raw_count: int
    candidate_count: int
    excluded_count: int
    services: list[ServicePreprocessingResult] = Field(default_factory=list)
