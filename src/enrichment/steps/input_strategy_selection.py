from time import perf_counter

from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseEnrichmentPolicy, BaseEnrichmentStep


class InputStrategySelectionStep(BaseEnrichmentStep):
    name = "input_strategy_selection"

    def __init__(self, policy: BaseEnrichmentPolicy) -> None:
        self.policy = policy

    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        if context.stopped:
            return context
        started_at = perf_counter()
        context.result = self.policy.decide(context)
        context.record.selection_duration_ms = round((perf_counter() - started_at) * 1000)
        context.record.status = context.result.status
        context.record.input_strategy = context.result.input_strategy
        context.record.input_strategy_reason = context.result.input_strategy_reason
        context.record.selected_chunk_count = len(context.result.selected_chunks)
        context.record.selected_token_count = sum(
            chunk.token_count for chunk in context.result.selected_chunks
        )
        context.record.failure_reason = context.result.failure_reason
        context.record.failure_detail = context.result.failure_detail
        return context
