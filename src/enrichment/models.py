from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field

from src.processing.models import ArticleCandidate


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


class DocumentBlockType(StrEnum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST_ITEM = "list_item"
    CODE = "code"
    QUOTE = "quote"
    TABLE = "table"
    OTHER = "other"


class FetchedContent(BaseModel):
    source_url: str
    final_url: str
    http_status: int = Field(ge=100, le=599)
    content_type: str
    body: str
    response_bytes: int = Field(ge=0)
    duration_ms: int = Field(ge=0)
    attempt_count: int = Field(default=1, ge=1)


class DocumentBlock(BaseModel):
    block_id: str
    block_type: DocumentBlockType
    heading_path: list[str] = Field(default_factory=list)
    text: str
    position: int = Field(ge=0)
    token_count: int = Field(ge=0)


class ExtractedDocument(BaseModel):
    title: str | None = None
    author: str | None = None
    published_at: str | None = None
    detected_language: str | None = None
    document_type: str = "article"
    plain_text: str
    content_hash: str
    char_count: int = Field(ge=0)
    token_count: int = Field(ge=0)
    blocks: list[DocumentBlock] = Field(default_factory=list)


class EvidenceChunk(BaseModel):
    chunk_id: str
    heading_path: list[str] = Field(default_factory=list)
    text: str
    block_ids: list[str] = Field(default_factory=list)
    token_count: int = Field(ge=0)
    position: int = Field(ge=0)


class EnrichedArticleCandidate(BaseModel):
    candidate: ArticleCandidate
    status: EnrichmentStatus
    input_strategy: EnrichmentInputStrategy
    input_strategy_reason: str | None = None
    document: ExtractedDocument | None = None
    chunks: list[EvidenceChunk] = Field(default_factory=list)
    selected_chunks: list[EvidenceChunk] = Field(default_factory=list)
    failure_reason: EnrichmentFailureReason | None = None
    failure_detail: str | None = None


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
    candidates: list[EnrichedArticleCandidate] = Field(default_factory=list)
