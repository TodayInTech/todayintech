from typing import Protocol

from src.enrichment.models import EnrichmentResult
from src.writer.agent.schemas import EditorialResult


class NewsEditorAgent(Protocol):
    def edit(self, enrichment_result: EnrichmentResult) -> EditorialResult:
        """Create an editorial result from enriched candidates."""
        ...
