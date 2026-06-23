from pydantic import BaseModel, ConfigDict, Field

from src.enrichment.models import (
    EnrichedArticleCandidate,
    EnrichmentFailureReason,
    EnrichmentInputStrategy,
    EnrichmentRecord,
    EnrichmentStatus,
    EvidenceChunk,
    ExtractedDocument,
    FetchedContent,
)
from src.processing.models import ArticleCandidate


class EnrichmentContext(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    candidate: ArticleCandidate
    record: EnrichmentRecord
    fetched_content: FetchedContent | None = None
    extracted_document: ExtractedDocument | None = None
    chunks: list[EvidenceChunk] = Field(default_factory=list)
    result: EnrichedArticleCandidate | None = None

    @property
    def stopped(self) -> bool:
        return self.result is not None

    def fail(
        self,
        reason: EnrichmentFailureReason,
        detail: str,
        *,
        allow_fallback: bool = True,
    ) -> None:
        self.record.failure_reason = reason
        self.record.failure_detail = detail
        feed_summary = self.candidate.feed_summary.strip()
        if allow_fallback and len(feed_summary) >= 80:
            self.result = EnrichedArticleCandidate(
                candidate=self.candidate,
                status=EnrichmentStatus.FALLBACK,
                input_strategy=EnrichmentInputStrategy.FEED_METADATA_ONLY,
                input_strategy_reason=f"{reason.value}: feed metadata fallback",
                failure_reason=reason,
                failure_detail=detail,
            )
            return

        self.result = EnrichedArticleCandidate(
            candidate=self.candidate,
            status=EnrichmentStatus.FAILED,
            input_strategy=EnrichmentInputStrategy.NONE,
            input_strategy_reason=reason.value,
            failure_reason=reason,
            failure_detail=detail,
        )
