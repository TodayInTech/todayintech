from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl


class NewsCategory(StrEnum):
    AI = "AI"
    CLOUD = "Cloud"
    DEVELOPER_TOOLS = "Developer Tools"
    SECURITY = "Security"
    OPEN_SOURCE = "Open Source"
    BUSINESS = "Business"
    RESEARCH = "Research"
    OTHER = "Other"


class Article(BaseModel):
    source: str
    title: str
    url: HttpUrl
    published_at: datetime | None = None
    collected_at: datetime
    summary: str | None = None
    authors: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


class ArticleSummary(BaseModel):
    article: Article
    category: NewsCategory = NewsCategory.OTHER
    importance_score: int = Field(ge=1, le=5)
    importance_reason: str
    summary_ko: str
    why_it_matters_ko: str


class ServiceBriefing(BaseModel):
    service_key: str
    service_name: str
    generated_for: str
    summaries: list[ArticleSummary] = Field(default_factory=list)


class BriefingBundle(BaseModel):
    generated_for: str
    service_briefings: list[ServiceBriefing] = Field(default_factory=list)
    insight_ko: str = ""


class ServiceCollectionResult(BaseModel):
    service_key: str
    service_name: str
    source_url: str
    collection_method: str
    collected_at: datetime
    status: str
    duration_ms: int = Field(ge=0)
    articles: list[Article] = Field(default_factory=list)
    warning_codes: list[str] = Field(default_factory=list)
    error: str | None = None
