from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field

from src.processing.models import RankingSignals


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
    ranking_signals: RankingSignals = Field(default_factory=RankingSignals)
    ranking_reasons_ko: list[str] = Field(default_factory=list)
    suggested_doc_key: str
    article_doc_path: str
    editorial_status: EditorialStatus
    generation_method: GenerationMethod
    category: str | None = None
    importance_level: str | None = None
    confidence_score: float | None = None
    summary_scope: str | None = None
    publish_reason_ko: str | None = None
    reject_reason_ko: str | None = None
    evidence_basis_ko: list[str] = Field(default_factory=list)
    briefing_body_ko: str | None = None
    key_points_ko: list[str] = Field(default_factory=list)
    why_it_matters_ko: str | None = None
    caveats_ko: list[str] = Field(default_factory=list)


class ServiceWritingResult(BaseModel):
    service_key: str
    service_name: str
    briefings: list[ArticleBriefing] = Field(default_factory=list)


class EditorialResult(BaseModel):
    generated_for: str
    services: list[ServiceWritingResult] = Field(default_factory=list)
