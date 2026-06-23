from time import perf_counter

import httpx

from src.enrichment.contracts import BaseContentFetcher
from src.enrichment.errors import EnrichmentError
from src.enrichment.models import EnrichmentFailureReason, FetchedContent


class HttpContentFetcher(BaseContentFetcher):
    name = "http"

    def __init__(
        self,
        *,
        timeout_seconds: float = 20,
        max_attempts: int = 2,
        user_agent: str = "TodayInTech/0.1 (+https://github.com/TodayInTech/todayintech)",
        client: httpx.Client | None = None,
    ) -> None:
        self.timeout_seconds = timeout_seconds
        self.max_attempts = max(max_attempts, 1)
        self.client = client or httpx.Client(
            follow_redirects=True,
            timeout=timeout_seconds,
            headers={"User-Agent": user_agent},
        )

    def fetch(self, url: str) -> FetchedContent:
        last_error: Exception | None = None
        for attempt in range(1, self.max_attempts + 1):
            started_at = perf_counter()
            try:
                response = self.client.get(url)
            except httpx.TimeoutException as exc:
                last_error = exc
                if attempt < self.max_attempts:
                    continue
                raise EnrichmentError(
                    EnrichmentFailureReason.FETCH_TIMEOUT,
                    f"Source request timed out after {attempt} attempts",
                ) from exc
            except httpx.HTTPError as exc:
                last_error = exc
                if attempt < self.max_attempts:
                    continue
                raise EnrichmentError(
                    EnrichmentFailureReason.FETCH_FAILED,
                    f"Source request failed: {type(exc).__name__}",
                ) from exc

            duration_ms = round((perf_counter() - started_at) * 1000)
            content_type = response.headers.get("content-type", "").split(";", 1)[0].lower()
            if response.status_code in {401, 403}:
                raise EnrichmentError(
                    EnrichmentFailureReason.ACCESS_DENIED,
                    f"Source returned HTTP {response.status_code}",
                    http_status=response.status_code,
                    content_type=content_type,
                )
            if response.status_code == 429:
                raise EnrichmentError(
                    EnrichmentFailureReason.RATE_LIMITED,
                    "Source returned HTTP 429",
                    http_status=response.status_code,
                    content_type=content_type,
                )
            if response.status_code >= 400:
                raise EnrichmentError(
                    EnrichmentFailureReason.FETCH_FAILED,
                    f"Source returned HTTP {response.status_code}",
                    http_status=response.status_code,
                    content_type=content_type,
                )
            if content_type not in {"text/html", "application/xhtml+xml", ""}:
                raise EnrichmentError(
                    EnrichmentFailureReason.UNSUPPORTED_CONTENT_TYPE,
                    f"Unsupported content type: {content_type or 'unknown'}",
                    http_status=response.status_code,
                    content_type=content_type,
                )
            return FetchedContent(
                source_url=url,
                final_url=str(response.url),
                http_status=response.status_code,
                content_type=content_type or "text/html",
                body=response.text,
                response_bytes=len(response.content),
                duration_ms=duration_ms,
                attempt_count=attempt,
            )

        raise EnrichmentError(
            EnrichmentFailureReason.FETCH_FAILED,
            f"Source request failed: {last_error}",
        )
