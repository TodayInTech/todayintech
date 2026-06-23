from datetime import UTC, datetime

from src.enrichment.models import (
    EnrichmentFailureReason,
    EnrichmentInputStrategy,
    EnrichmentRecord,
    EnrichmentResult,
    EnrichmentStatus,
)
from src.tracing.enrichment_trace import build_enrichment_trace, write_enrichment_trace


def make_record(
    *,
    candidate_id: str,
    status: EnrichmentStatus,
    strategy: EnrichmentInputStrategy,
    token_count: int = 0,
    selected_token_count: int = 0,
    failure_reason: EnrichmentFailureReason | None = None,
) -> EnrichmentRecord:
    return EnrichmentRecord(
        candidate_id=candidate_id,
        service_key="openai-blog",
        service_name="OpenAI Blog",
        title="OpenAI Developer Update",
        source_url=f"https://openai.com/news/{candidate_id}",
        final_url=f"https://openai.com/index/{candidate_id}",
        status=status,
        input_strategy=strategy,
        input_strategy_reason="token_budget_policy",
        http_status=200,
        content_type="text/html",
        response_bytes=12000,
        fetch_duration_ms=80,
        extraction_duration_ms=20,
        selection_duration_ms=10,
        extractor_name="trafilatura",
        extractor_version="2.1.0",
        content_hash=f"sha256:{candidate_id}",
        document_type="technical_article",
        detected_language="en",
        extracted_char_count=token_count * 4,
        extracted_token_count=token_count,
        section_count=4,
        chunk_count=6,
        code_block_count=1,
        list_item_count=3,
        selected_chunk_count=2 if selected_token_count else 0,
        selected_token_count=selected_token_count,
        title_similarity=0.92,
        extraction_quality_score=0.88,
        failure_reason=failure_reason,
    )


def make_result() -> EnrichmentResult:
    return EnrichmentResult(
        generated_for="2026-06-23",
        generated_at=datetime(2026, 6, 23, tzinfo=UTC),
        duration_ms=240,
        records=[
            make_record(
                candidate_id="full",
                status=EnrichmentStatus.ENRICHED,
                strategy=EnrichmentInputStrategy.FULL_CONTENT,
                token_count=1000,
                selected_token_count=1000,
            ),
            make_record(
                candidate_id="selected",
                status=EnrichmentStatus.ENRICHED,
                strategy=EnrichmentInputStrategy.CHUNK_SELECTION,
                token_count=5000,
                selected_token_count=1800,
            ),
            make_record(
                candidate_id="fallback",
                status=EnrichmentStatus.FALLBACK,
                strategy=EnrichmentInputStrategy.FEED_METADATA_ONLY,
                failure_reason=EnrichmentFailureReason.ACCESS_DENIED,
            ),
            make_record(
                candidate_id="failed",
                status=EnrichmentStatus.FAILED,
                strategy=EnrichmentInputStrategy.NONE,
                failure_reason=EnrichmentFailureReason.THIN_CONTENT,
            ),
        ],
    )


def test_build_enrichment_trace_aggregates_quality_and_strategy_metrics() -> None:
    trace = build_enrichment_trace(make_result())

    assert trace["stage"] == "enrichment"
    assert trace["status"] == "partial"
    assert trace["candidate_count"] == 4
    assert trace["usable_count"] == 3
    assert trace["usable_rate"] == 75.0
    assert trace["cache_hit_rate"] == 0
    assert trace["policy_name"] == "default"
    assert trace["policy_version"] == "1"
    assert trace["status_counts"] == {"enriched": 2, "failed": 1, "fallback": 1}
    assert trace["input_strategy_counts"] == {
        "chunk_selection": 1,
        "feed_metadata_only": 1,
        "full_content": 1,
        "none": 1,
    }
    assert trace["failure_reason_counts"] == {"access_denied": 1, "thin_content": 1}
    assert trace["document_type_counts"] == {"technical_article": 4}
    assert trace["total_extracted_token_count"] == 6000
    assert trace["total_selected_token_count"] == 2800
    assert trace["selected_token_ratio"] == 0.4667
    assert trace["fetch_duration_distribution_ms"]["p50"] == 80
    assert trace["extraction_duration_distribution_ms"]["p90"] == 20
    assert trace["extracted_token_distribution"]["p50"] == 3000
    assert trace["extracted_token_distribution"]["p90"] == 4600
    assert trace["records"][1]["selected_token_ratio"] == 0.36
    assert trace["services"][0]["usable_rate"] == 75.0


def test_build_enrichment_trace_treats_empty_run_as_successful_noop() -> None:
    result = EnrichmentResult(
        generated_for="2026-06-23",
        generated_at=datetime(2026, 6, 23, tzinfo=UTC),
    )

    trace = build_enrichment_trace(result)

    assert trace["status"] == "success"
    assert trace["candidate_count"] == 0


def test_write_enrichment_trace_outputs_json_and_markdown(tmp_path) -> None:
    written_paths = write_enrichment_trace(tmp_path, make_result())

    json_path = tmp_path / "2026-06-23" / "enrichment.json"
    markdown_path = tmp_path / "2026-06-23" / "enrichment-summary.md"
    assert written_paths == [json_path, markdown_path]
    assert json_path.exists()
    assert markdown_path.exists()
    assert "Usable candidates: 3 (75.0%)" in markdown_path.read_text(encoding="utf-8")
