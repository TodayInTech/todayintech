import base64
from time import perf_counter, sleep

import httpx

from src.enrichment.contracts import BaseContentFetcher
from src.enrichment.errors import EnrichmentError
from src.enrichment.fetchers.urls import alternate_article_url, download_url
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
        started_at = perf_counter()
        request_url = download_url(url)
        for attempt in range(1, self.max_attempts + 1):
            try:
                with self.client.stream("GET", request_url) as response:
                    status = response.status_code
                    content_type = (
                        response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
                    )
                    if status >= 400:
                        reason = (
                            EnrichmentFailureReason.ACCESS_DENIED
                            if status in {401, 403}
                            else EnrichmentFailureReason.RATE_LIMITED
                            if status == 429
                            else EnrichmentFailureReason.FETCH_FAILED
                        )
                        alternate = (
                            alternate_article_url(request_url) if status in {403, 404} else None
                        )
                        if attempt < self.max_attempts and alternate:
                            request_url = alternate
                            continue
                        if attempt < self.max_attempts and (status == 429 or status >= 500):
                            try:
                                delay = float(response.headers.get("retry-after", "1"))
                            except ValueError:
                                delay = None
                            # Do not retry sooner than a publisher's long Retry-After.
                            if delay is not None and 0 <= delay <= 5:
                                sleep(delay)
                                continue
                        raise EnrichmentError(
                            reason,
                            f"Source returned HTTP {status}",
                            http_status=status,
                            content_type=content_type,
                        )
                    if content_type not in {
                        "text/html",
                        "application/xhtml+xml",
                        "application/pdf",
                        "application/octet-stream",
                        "",
                    }:
                        raise EnrichmentError(
                            EnrichmentFailureReason.UNSUPPORTED_CONTENT_TYPE,
                            f"Unsupported content type: {content_type}",
                            http_status=status,
                            content_type=content_type,
                        )
                    chunks = []
                    size = 0
                    for chunk in response.iter_bytes():
                        size += len(chunk)
                        if size > 20 * 1024 * 1024:
                            raise EnrichmentError(
                                EnrichmentFailureReason.POLICY_REJECTED,
                                "Source exceeds 20 MiB download limit",
                                http_status=status,
                                content_type=content_type,
                            )
                        chunks.append(chunk)
                    content = b"".join(chunks)
                    is_pdf = content.startswith(b"%PDF-")
                    if (
                        content_type in {"application/pdf", "application/octet-stream"}
                        and not is_pdf
                    ):
                        raise EnrichmentError(
                            EnrichmentFailureReason.UNSUPPORTED_CONTENT_TYPE,
                            "Binary response is not a PDF",
                            http_status=status,
                            content_type=content_type,
                        )
                    return FetchedContent(
                        source_url=url,
                        final_url=str(response.url),
                        http_status=status,
                        content_type="application/pdf" if is_pdf else content_type or "text/html",
                        body=""
                        if is_pdf
                        else content.decode(response.encoding or "utf-8", errors="replace"),
                        binary_base64=base64.b64encode(content).decode("ascii") if is_pdf else None,
                        response_bytes=size,
                        duration_ms=round((perf_counter() - started_at) * 1000),
                        attempt_count=attempt,
                    )
            except httpx.HTTPError as exc:
                if attempt < self.max_attempts:
                    continue
                reason = (
                    EnrichmentFailureReason.FETCH_TIMEOUT
                    if isinstance(exc, httpx.TimeoutException)
                    else EnrichmentFailureReason.FETCH_FAILED
                )
                raise EnrichmentError(
                    reason, f"Source request failed after {attempt} attempts: {type(exc).__name__}"
                ) from exc
        raise EnrichmentError(EnrichmentFailureReason.FETCH_FAILED, "Source request exhausted")
