from datetime import datetime

from pydantic import BaseModel, Field

from src.models import Article
from src.processing.enums import ExcludedReason


class RankingSignals(BaseModel):
    source_priority: int = 0
    age_days: int | None = None
    freshness_score: float = 0
    high_signal_count: int = 0
    low_signal_count: int = 0
    hn_points_score: float | None = None
    hn_comments_score: float | None = None
    rss_rank_score: float | None = None

    def compact_dict(self) -> dict[str, int | float]:
        return self.model_dump(exclude_none=True)


class ArticleCandidate(BaseModel):
    candidate_id: str = ""
    service_key: str
    service_name: str
    article: Article
    normalized_url: str = ""
    url_hash: str = ""
    title_fingerprint: str = ""
    feed_summary: str = ""
    suggested_doc_key: str = ""
    suggested_article_path: str = ""
    candidate_score: float = 0
    ranking_signals: RankingSignals = Field(default_factory=RankingSignals)
    excluded_reason: ExcludedReason | None = None


class PreprocessingStepMetrics(BaseModel):
    step_name: str
    input_count: int
    output_count: int
    excluded_count: int
    duration_ms: int = Field(ge=0)
    reason_counts: dict[ExcludedReason, int] = Field(default_factory=dict)


class ServicePreprocessingResult(BaseModel):
    service_key: str
    service_name: str
    raw_count: int
    candidate_count: int
    excluded_count: int
    candidates: list[ArticleCandidate] = Field(default_factory=list)
    excluded: list[ArticleCandidate] = Field(default_factory=list)


class ArchivedArticle(BaseModel):
    service_key: str
    service_name: str
    title: str
    article_doc_path: str
    status: str
    briefed_at: datetime | None = None
    candidate_score: float = 0


class PreprocessingResult(BaseModel):
    generated_for: str
    generated_at: datetime
    duration_ms: int = Field(default=0, ge=0)
    raw_count: int
    candidate_count: int
    excluded_count: int
    step_metrics: list[PreprocessingStepMetrics] = Field(default_factory=list)
    services: list[ServicePreprocessingResult] = Field(default_factory=list)
    archived_articles: list[ArchivedArticle] = Field(default_factory=list)
