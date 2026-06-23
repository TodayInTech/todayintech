from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseEnrichmentStep
from src.enrichment.models import DocumentBlockType


class DocumentProfilingStep(BaseEnrichmentStep):
    name = "document_profiling"

    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        if context.stopped:
            return context
        document = context.extracted_document
        if document is None:
            return context

        block_counts = {
            block_type: sum(block.block_type == block_type for block in document.blocks)
            for block_type in DocumentBlockType
        }
        context.record.content_hash = document.content_hash
        context.record.document_type = document.document_type
        context.record.detected_language = document.detected_language
        context.record.extracted_char_count = document.char_count
        context.record.extracted_token_count = document.token_count
        context.record.section_count = block_counts[DocumentBlockType.HEADING]
        context.record.code_block_count = block_counts[DocumentBlockType.CODE]
        context.record.table_count = block_counts[DocumentBlockType.TABLE]
        context.record.list_item_count = block_counts[DocumentBlockType.LIST_ITEM]

        token_score = min(document.token_count / 1000, 1)
        title_score = context.record.title_similarity
        context.record.extraction_quality_score = round(
            token_score if title_score is None else token_score * 0.7 + title_score * 0.3,
            4,
        )
        return context
