from datetime import UTC, datetime

from src.models import ServiceCollectionResult
from src.tracing.collection_trace import build_collection_trace, write_collection_trace


def make_result(
    service_key: str = "hacker-news",
    status: str = "success",
    duration_ms: int = 12,
) -> ServiceCollectionResult:
    return ServiceCollectionResult(
        service_key=service_key,
        service_name="Hacker News",
        source_url="https://hnrss.org/frontpage",
        collection_method="rss",
        collected_at=datetime.now(UTC),
        status=status,
        duration_ms=duration_ms,
        articles=[],
        warning_codes=["empty_collection"],
    )


def test_collection_trace_includes_duration_and_warnings() -> None:
    trace = build_collection_trace("2026-06-07", [make_result()])

    assert trace["stage"] == "collection"
    assert trace["duration_ms"] == 12
    assert trace["warning_count"] == 1
    assert trace["total_article_count"] == 0


def test_write_collection_trace_outputs_json_and_markdown(tmp_path) -> None:
    written_paths = write_collection_trace(tmp_path, "2026-06-07", [make_result()])

    assert tmp_path.joinpath("2026-06-07", "collection.json") in written_paths
    assert tmp_path.joinpath("2026-06-07", "summary.md") in written_paths
    assert tmp_path.joinpath("2026-06-07", "collection.json").exists()
    assert tmp_path.joinpath("2026-06-07", "summary.md").exists()
