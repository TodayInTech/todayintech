from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class EditorialStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"


class GenerationMethod(StrEnum):
    DRAFT = "draft"
    LLM = "llm"


class ArticleBriefing(BaseModel):
    candidate_id: str
    service_key: str
    service_name: str
    title: str
    source_url: str
    normalized_url: str
    title_fingerprint: str
    published_at: datetime | None = None
    collected_at: datetime
    feed_summary: str = ""
    candidate_score: float
    ranking_signals: dict[str, str | int | float | bool] = Field(default_factory=dict)
    suggested_doc_key: str
    article_doc_path: str
    editorial_status: EditorialStatus
    generation_method: GenerationMethod
    summary_ko: str | None = None
    why_it_matters_ko: str | None = None
    developer_insight_ko: str | None = None


class ServiceWritingResult(BaseModel):
    service_key: str
    service_name: str
    briefings: list[ArticleBriefing] = Field(default_factory=list)


class EditorialResult(BaseModel):
    generated_for: str
    services: list[ServiceWritingResult] = Field(default_factory=list)
