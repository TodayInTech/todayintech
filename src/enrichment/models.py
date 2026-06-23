from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class EnrichmentStatus(StrEnum):
    ENRICHED = "enriched"
    FALLBACK = "fallback"
    SKIPPED = "skipped"
    FAILED = "failed"


class EnrichmentInputStrategy(StrEnum):
    FULL_CONTENT = "full_content"
    CHUNK_SELECTION = "chunk_selection"
    EVIDENCE_SELECTION = "evidence_selection"
    FEED_METADATA_ONLY = "feed_metadata_only"
    NONE = "none"


class EnrichmentFailureReason(StrEnum):
    FETCH_FAILED = "fetch_failed"
    FETCH_TIMEOUT = "fetch_timeout"
    ACCESS_DENIED = "access_denied"
    RATE_LIMITED = "rate_limited"
    UNSUPPORTED_CONTENT_TYPE = "unsupported_content_type"
    EMPTY_CONTENT = "empty_content"
    THIN_CONTENT = "thin_content"
    TITLE_MISMATCH = "title_mismatch"
    EXTRACTION_FAILED = "extraction_failed"
    SELECTION_FAILED = "selection_failed"
    POLICY_REJECTED = "policy_rejected"
    UNKNOWN = "unknown"


class EnrichmentRecord(BaseModel):
    candidate_id: str
    service_key: str
    service_name: str
    title: str
    source_url: str
    final_url: str | None = None
    status: EnrichmentStatus
    input_strategy: EnrichmentInputStrategy
    input_strategy_reason: str | None = None
    cache_hit: bool = False
    fetch_attempt_count: int = Field(default=1, ge=0)
    http_status: int | None = Field(default=None, ge=100, le=599)
    content_type: str | None = None
    response_bytes: int = Field(default=0, ge=0)
    fetch_duration_ms: int = Field(default=0, ge=0)
    extraction_duration_ms: int = Field(default=0, ge=0)
    selection_duration_ms: int = Field(default=0, ge=0)
    extractor_name: str | None = None
    extractor_version: str | None = None
    content_hash: str | None = None
    document_type: str | None = None
    detected_language: str | None = None
    extracted_char_count: int = Field(default=0, ge=0)
    extracted_token_count: int = Field(default=0, ge=0)
    section_count: int = Field(default=0, ge=0)
    chunk_count: int = Field(default=0, ge=0)
    code_block_count: int = Field(default=0, ge=0)
    table_count: int = Field(default=0, ge=0)
    list_item_count: int = Field(default=0, ge=0)
    selected_chunk_count: int = Field(default=0, ge=0)
    selected_token_count: int = Field(default=0, ge=0)
    title_similarity: float | None = Field(default=None, ge=0, le=1)
    extraction_quality_score: float | None = Field(default=None, ge=0, le=1)
    failure_reason: EnrichmentFailureReason | None = None
    failure_detail: str | None = None


class EnrichmentResult(BaseModel):
    generated_for: str
    generated_at: datetime
    duration_ms: int = Field(default=0, ge=0)
    policy_name: str = "default"
    policy_version: str = "1"
    records: list[EnrichmentRecord] = Field(default_factory=list)
