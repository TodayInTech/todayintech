from time import perf_counter

from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseContentExtractor, BaseEnrichmentStep
from src.enrichment.errors import EnrichmentError
from src.enrichment.models import EnrichmentFailureReason


class ContentExtractionStep(BaseEnrichmentStep):
    name = "content_extraction"

    def __init__(self, extractor: BaseContentExtractor) -> None:
        self.extractor = extractor

    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        if context.stopped:
            return context
        if context.fetched_content is None:
            context.fail(
                EnrichmentFailureReason.EXTRACTION_FAILED,
                "Fetched content is unavailable",
            )
            return context

        started_at = perf_counter()
        try:
            document = self.extractor.extract(context.fetched_content)
        except EnrichmentError as exc:
            context.record.extraction_duration_ms = round((perf_counter() - started_at) * 1000)
            context.fail(exc.reason, exc.detail)
            return context

        context.record.extraction_duration_ms = round((perf_counter() - started_at) * 1000)
        context.record.extractor_name = self.extractor.name
        context.record.extractor_version = self.extractor.version
        context.extracted_document = document
        return context
