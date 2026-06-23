from src.enrichment.contracts import BaseContentFetcher
from src.enrichment.fetchers import HttpContentFetcher


class ContentFetcherFactory:
    def create_http(
        self,
        *,
        timeout_seconds: float,
        max_attempts: int,
    ) -> BaseContentFetcher:
        return HttpContentFetcher(
            timeout_seconds=timeout_seconds,
            max_attempts=max_attempts,
        )
