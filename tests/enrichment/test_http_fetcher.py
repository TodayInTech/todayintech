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


def test_access_denied_retries_official_canonical_path_only():
    paths = []

    def handler(request):
        paths.append(request.url.path)
        if len(paths) == 1:
            return httpx.Response(403)
        return httpx.Response(
            200, headers={"content-type": "text/html"}, text="<article>original</article>"
        )

    fetched = HttpContentFetcher(client=httpx.Client(transport=httpx.MockTransport(handler))).fetch(
        "https://openai.com/index/decisions-api"
    )
    assert paths == ["/index/decisions-api", "/index/decisions-api/"]
    assert fetched.attempt_count == 2
    assert fetched.source_url == "https://openai.com/index/decisions-api"
    assert fetched.final_url.endswith("/decisions-api/")


def test_github_pdf_uses_original_binary_not_html_viewer():
    def handler(request):
        assert request.url.host == "raw.githubusercontent.com"
        assert request.url.path == "/openai/math/main/preprints/paper.pdf"
        return httpx.Response(
            200, headers={"content-type": "application/octet-stream"}, content=b"%PDF-1.7\noriginal"
        )

    fetched = HttpContentFetcher(client=httpx.Client(transport=httpx.MockTransport(handler))).fetch(
        "https://github.com/openai/math/blob/main/preprints/paper.pdf"
    )
    assert fetched.content_type == "application/pdf"
    assert fetched.binary_base64
    assert fetched.body == ""


def test_rate_limit_respects_long_retry_after_without_immediate_retry():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(429, headers={"Retry-After": "300"})

    with pytest.raises(EnrichmentError) as error:
        HttpContentFetcher(client=httpx.Client(transport=httpx.MockTransport(handler))).fetch(
            "https://example.com/article"
        )
    assert len(calls) == 1
    assert error.value.reason == EnrichmentFailureReason.RATE_LIMITED


def test_transient_server_failure_is_retried(monkeypatch):
    delays = []
    monkeypatch.setattr("src.enrichment.fetchers.http.sleep", delays.append)
    calls = []

    def handler(request):
        calls.append(request)
        return (
            httpx.Response(503)
            if len(calls) == 1
            else httpx.Response(200, headers={"content-type": "text/html"}, text="article")
        )

    fetched = HttpContentFetcher(client=httpx.Client(transport=httpx.MockTransport(handler))).fetch(
        "https://example.com/article"
    )
    assert fetched.attempt_count == 2
    assert delays == [1]


def test_pdf_mime_with_html_challenge_is_rejected():
    client = httpx.Client(
        transport=httpx.MockTransport(
            lambda _: httpx.Response(
                200, headers={"content-type": "application/pdf"}, text="<html>Sign in</html>"
            )
        )
    )
    with pytest.raises(EnrichmentError):
        HttpContentFetcher(client=client).fetch("https://example.com/paper.pdf")


def test_http_date_retry_after_is_not_retried_early(monkeypatch):
    delays = []
    monkeypatch.setattr("src.enrichment.fetchers.http.sleep", delays.append)
    client = httpx.Client(
        transport=httpx.MockTransport(
            lambda _: httpx.Response(429, headers={"Retry-After": "Fri, 30 Oct 2026 12:00:00 GMT"})
        )
    )
    with pytest.raises(EnrichmentError):
        HttpContentFetcher(client=client).fetch("https://example.com/article")
    assert delays == []


def test_download_limit_rejects_oversize_content():
    client = httpx.Client(
        transport=httpx.MockTransport(
            lambda _: httpx.Response(
                200, headers={"content-type": "text/html"}, content=b"x" * (20 * 1024 * 1024 + 1)
            )
        )
    )
    with pytest.raises(EnrichmentError) as error:
        HttpContentFetcher(client=client).fetch("https://example.com/article")
    assert error.value.reason == EnrichmentFailureReason.POLICY_REJECTED
