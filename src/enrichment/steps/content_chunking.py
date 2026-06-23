from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseContentChunker, BaseEnrichmentStep


class ContentChunkingStep(BaseEnrichmentStep):
    name = "content_chunking"

    def __init__(self, chunker: BaseContentChunker) -> None:
        self.chunker = chunker

    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        if context.stopped or context.extracted_document is None:
            return context
        context.chunks = self.chunker.chunk(context.extracted_document)
        context.record.chunk_count = len(context.chunks)
        return context
