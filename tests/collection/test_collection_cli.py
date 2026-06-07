from datetime import UTC, datetime

from src.collection.__main__ import should_fail_collection
from src.models import ServiceCollectionResult


def make_result(service_key: str, status: str) -> ServiceCollectionResult:
    return ServiceCollectionResult(
        service_key=service_key,
        service_name=service_key,
        source_url="https://example.com",
        collection_method="rss",
        collected_at=datetime.now(UTC),
        status=status,
        duration_ms=1,
    )


def test_collection_cli_succeeds_when_at_least_one_service_succeeds() -> None:
    results = [
        make_result("hacker-news", "success"),
        make_result("anthropic-blog", "failed"),
    ]

    assert should_fail_collection(results) is False


def test_collection_cli_fails_when_all_services_fail() -> None:
    results = [
        make_result("hacker-news", "failed"),
        make_result("anthropic-blog", "failed"),
    ]

    assert should_fail_collection(results) is True
