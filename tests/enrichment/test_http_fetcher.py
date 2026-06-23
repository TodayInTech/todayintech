import httpx
import pytest

from src.enrichment.errors import EnrichmentError
from src.enrichment.fetchers import HttpContentFetcher
from src.enrichment.models import EnrichmentFailureReason


def test_http_fetcher_returns_html_with_redirected_url() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            request=request,
            headers={"content-type": "text/html; charset=utf-8"},
            text="<html><body>article</body></html>",
        )

    fetcher = HttpContentFetcher(client=httpx.Client(transport=httpx.MockTransport(handler)))

    fetched = fetcher.fetch("https://example.com/article")

    assert fetched.http_status == 200
    assert fetched.content_type == "text/html"
    assert fetched.response_bytes > 0
    assert fetched.attempt_count == 1


def test_http_fetcher_normalizes_access_denied_failure() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(403, request=request)

    fetcher = HttpContentFetcher(client=httpx.Client(transport=httpx.MockTransport(handler)))

    with pytest.raises(EnrichmentError) as exc_info:
        fetcher.fetch("https://example.com/private")

    assert exc_info.value.reason == EnrichmentFailureReason.ACCESS_DENIED
    assert exc_info.value.http_status == 403
