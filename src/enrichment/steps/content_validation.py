from difflib import SequenceMatcher

from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseEnrichmentStep
from src.enrichment.models import EnrichmentFailureReason


class ContentValidationStep(BaseEnrichmentStep):
    name = "content_validation"

    def __init__(self, minimum_title_similarity: float = 0.15) -> None:
        self.minimum_title_similarity = minimum_title_similarity

    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        if context.stopped:
            return context
        document = context.extracted_document
        if document is None:
            return context

        extracted_title = (document.title or "").strip().lower()
        candidate_title = context.candidate.article.title.strip().lower()
        similarity = (
            SequenceMatcher(None, candidate_title, extracted_title).ratio()
            if extracted_title
            else None
        )
        context.record.title_similarity = similarity
        if similarity is not None and similarity < self.minimum_title_similarity:
            context.fail(
                EnrichmentFailureReason.TITLE_MISMATCH,
                f"Title similarity {similarity:.3f} is below threshold",
            )
        return context
