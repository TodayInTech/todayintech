from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseEnrichmentPolicy
from src.enrichment.models import (
    EnrichedArticleCandidate,
    EnrichmentFailureReason,
    EnrichmentInputStrategy,
    EnrichmentStatus,
)


class AdaptiveEnrichmentPolicy(BaseEnrichmentPolicy):
    name = "adaptive-token-budget"

    def __init__(
        self,
        *,
        minimum_tokens: int = 100,
        full_content_max_tokens: int = 4000,
        chunk_selection_max_tokens: int = 8000,
    ) -> None:
        self.minimum_tokens = minimum_tokens
        self.full_content_max_tokens = full_content_max_tokens
        self.chunk_selection_max_tokens = chunk_selection_max_tokens
        self.version = (
            f"1:min={minimum_tokens}:full={full_content_max_tokens}:"
            f"select={chunk_selection_max_tokens}"
        )

    def decide(self, context: EnrichmentContext) -> EnrichedArticleCandidate:
        document = context.extracted_document
        if document is None:
            context.fail(
                EnrichmentFailureReason.EXTRACTION_FAILED,
                "No extracted document is available",
            )
            assert context.result is not None
            return context.result

        if document.token_count < self.minimum_tokens:
            context.fail(
                EnrichmentFailureReason.THIN_CONTENT,
                f"Extracted content has only {document.token_count} tokens",
            )
            assert context.result is not None
            return context.result

        if document.token_count <= self.full_content_max_tokens:
            strategy = EnrichmentInputStrategy.FULL_CONTENT
            selected_chunks = context.chunks
            reason = f"document_tokens<={self.full_content_max_tokens}"
        elif document.token_count <= self.chunk_selection_max_tokens:
            strategy = EnrichmentInputStrategy.CHUNK_SELECTION
            selected_chunks = []
            reason = (
                f"{self.full_content_max_tokens}<document_tokens<={self.chunk_selection_max_tokens}"
            )
        else:
            strategy = EnrichmentInputStrategy.EVIDENCE_SELECTION
            selected_chunks = []
            reason = f"document_tokens>{self.chunk_selection_max_tokens}"

        return EnrichedArticleCandidate(
            candidate=context.candidate,
            status=EnrichmentStatus.ENRICHED,
            input_strategy=strategy,
            input_strategy_reason=reason,
            document=document,
            chunks=context.chunks,
            selected_chunks=selected_chunks,
        )
