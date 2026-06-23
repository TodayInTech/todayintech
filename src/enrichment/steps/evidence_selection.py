from time import perf_counter

from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseEnrichmentStep, BaseEvidenceSelector
from src.enrichment.models import EnrichmentFailureReason, EnrichmentInputStrategy


class EvidenceSelectionStep(BaseEnrichmentStep):
    name = "evidence_selection"

    def __init__(self, selector: BaseEvidenceSelector) -> None:
        self.selector = selector

    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        result = context.result
        if result is None:
            return context
        if result.input_strategy not in {
            EnrichmentInputStrategy.CHUNK_SELECTION,
            EnrichmentInputStrategy.EVIDENCE_SELECTION,
        }:
            return context

        started_at = perf_counter()
        selected_chunks = self.selector.select(context)
        context.record.selection_duration_ms += round((perf_counter() - started_at) * 1000)
        if not selected_chunks:
            context.fail(
                EnrichmentFailureReason.SELECTION_FAILED,
                "No evidence chunks were selected for long-form content",
                allow_fallback=False,
            )
            return context

        context.result = result.model_copy(update={"selected_chunks": selected_chunks})
        context.record.selected_chunk_count = len(selected_chunks)
        context.record.selected_token_count = sum(chunk.token_count for chunk in selected_chunks)
        return context
