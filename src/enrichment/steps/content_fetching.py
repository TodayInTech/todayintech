from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseContentFetcher, BaseEnrichmentStep
from src.enrichment.errors import EnrichmentError


class ContentFetchingStep(BaseEnrichmentStep):
    name = "content_fetching"

    def __init__(self, fetcher: BaseContentFetcher) -> None:
        self.fetcher = fetcher

    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        if context.stopped:
            return context
        try:
            fetched = self.fetcher.fetch(context.candidate.normalized_url)
        except EnrichmentError as exc:
            context.record.http_status = exc.http_status
            context.record.content_type = exc.content_type
            context.fail(exc.reason, exc.detail)
            return context

        context.fetched_content = fetched
        context.record.final_url = fetched.final_url
        context.record.http_status = fetched.http_status
        context.record.content_type = fetched.content_type
        context.record.response_bytes = fetched.response_bytes
        context.record.fetch_duration_ms = fetched.duration_ms
        context.record.fetch_attempt_count = fetched.attempt_count
        return context
