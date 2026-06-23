from src.enrichment.contracts import (
    BaseContentChunker,
    BaseContentExtractor,
    BaseContentFetcher,
    BaseEnrichmentPolicy,
    BaseEnrichmentStep,
)
from src.enrichment.steps import (
    ContentChunkingStep,
    ContentExtractionStep,
    ContentFetchingStep,
    ContentValidationStep,
    DocumentProfilingStep,
    InputStrategySelectionStep,
)


class EnrichmentPipelineFactory:
    def create_default(
        self,
        *,
        fetcher: BaseContentFetcher,
        extractor: BaseContentExtractor,
        chunker: BaseContentChunker,
        policy: BaseEnrichmentPolicy,
    ) -> list[BaseEnrichmentStep]:
        return [
            ContentFetchingStep(fetcher),
            ContentExtractionStep(extractor),
            DocumentProfilingStep(),
            ContentValidationStep(),
            ContentChunkingStep(chunker),
            InputStrategySelectionStep(policy),
        ]
