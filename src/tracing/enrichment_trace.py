import json
import math
import os
from collections import Counter
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path

from src.enrichment.models import (
    EnrichmentInputStrategy,
    EnrichmentRecord,
    EnrichmentResult,
    EnrichmentStatus,
)


def build_enrichment_trace(result: EnrichmentResult) -> dict[str, object]:
    records = result.records
    status_counts = _count_values(record.status.value for record in records)
    strategy_counts = _count_values(record.input_strategy.value for record in records)
    failure_reason_counts = _count_values(
        record.failure_reason.value for record in records if record.failure_reason
    )
    usable_count = sum(
        record.status in {EnrichmentStatus.ENRICHED, EnrichmentStatus.FALLBACK}
        for record in records
    )
    writer_ready_count = sum(_is_writer_ready(record) for record in records)
    enriched_token_counts = [
        record.extracted_token_count
        for record in records
        if record.status == EnrichmentStatus.ENRICHED
    ]
    total_extracted_tokens = sum(record.extracted_token_count for record in records)
    total_selected_tokens = sum(record.selected_token_count for record in records)
    cache_hit_count = sum(record.cache_hit for record in records)

    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_for": result.generated_for,
        "stage": "enrichment",
        "status": _stage_status(records, usable_count),
        "git_sha": os.getenv("GITHUB_SHA"),
        "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "duration_ms": result.duration_ms,
        "policy_name": result.policy_name,
        "policy_version": result.policy_version,
        "candidate_count": len(records),
        "usable_count": usable_count,
        "usable_rate": _percentage(usable_count, len(records)),
        "writer_ready_count": writer_ready_count,
        "writer_ready_rate": _percentage(writer_ready_count, len(records)),
        "cache_hit_count": cache_hit_count,
        "cache_hit_rate": _percentage(cache_hit_count, len(records)),
        "status_counts": status_counts,
        "input_strategy_counts": strategy_counts,
        "document_type_counts": _count_values(
            record.document_type for record in records if record.document_type
        ),
        "failure_reason_counts": failure_reason_counts,
        "total_extracted_token_count": total_extracted_tokens,
        "total_selected_token_count": total_selected_tokens,
        "selected_token_ratio": _ratio(total_selected_tokens, total_extracted_tokens),
        "extracted_token_distribution": _token_distribution(enriched_token_counts),
        "fetch_duration_distribution_ms": _value_distribution(
            [record.fetch_duration_ms for record in records]
        ),
        "extraction_duration_distribution_ms": _value_distribution(
            [record.extraction_duration_ms for record in records]
        ),
        "selection_duration_distribution_ms": _value_distribution(
            [record.selection_duration_ms for record in records]
        ),
        "services": _service_summaries(records),
        "records": [_record_payload(record) for record in records],
    }


def build_enrichment_trace_markdown(trace: dict[str, object]) -> str:
    services = trace["services"]
    assert isinstance(services, list)
    token_distribution = trace["extracted_token_distribution"]
    assert isinstance(token_distribution, dict)
    status_counts = trace["status_counts"]
    assert isinstance(status_counts, dict)
    strategy_counts = trace["input_strategy_counts"]
    assert isinstance(strategy_counts, dict)
    failure_counts = trace["failure_reason_counts"]
    assert isinstance(failure_counts, dict)

    lines = [
        f"# Enrichment Trace - {trace['generated_for']}",
        "",
        "## Summary",
        "",
        f"- Status: `{trace['status']}`",
        f"- Policy: `{trace['policy_name']}@{trace['policy_version']}`",
        f"- Duration: {trace['duration_ms']} ms",
        f"- Candidates: {trace['candidate_count']}",
        f"- Usable candidates: {trace['usable_count']} ({trace['usable_rate']}%)",
        (
            f"- Writer-ready candidates: {trace['writer_ready_count']} "
            f"({trace['writer_ready_rate']}%)"
        ),
        f"- Status counts: {_format_counts(status_counts)}",
        f"- Input strategies: {_format_counts(strategy_counts)}",
        f"- Failure reasons: {_format_counts(failure_counts)}",
        (
            "- Extracted tokens: "
            f"p50 {token_distribution['p50']}, "
            f"p90 {token_distribution['p90']}, "
            f"max {token_distribution['max']}"
        ),
        "",
        "## Services",
        "",
        "| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for service in services:
        assert isinstance(service, dict)
        service_status_counts = service["status_counts"]
        assert isinstance(service_status_counts, dict)
        service_tokens = service["extracted_token_distribution"]
        assert isinstance(service_tokens, dict)
        lines.append(
            "| "
            f"{service['service_key']} | "
            f"{service['candidate_count']} | "
            f"{service['usable_count']} | "
            f"{service_status_counts.get('enriched', 0)} | "
            f"{service_status_counts.get('fallback', 0)} | "
            f"{service_status_counts.get('failed', 0)} | "
            f"{service_tokens['p50']} |"
        )

    lines.append("")
    return "\n".join(lines)


def write_enrichment_trace(
    trace_root_dir: Path,
    result: EnrichmentResult,
) -> list[Path]:
    output_dir = trace_root_dir / result.generated_for
    output_dir.mkdir(parents=True, exist_ok=True)

    trace = build_enrichment_trace(result)
    json_path = output_dir / "enrichment.json"
    markdown_path = output_dir / "enrichment-summary.md"

    json_path.write_text(
        json.dumps(trace, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    markdown_path.write_text(
        build_enrichment_trace_markdown(trace),
        encoding="utf-8",
    )
    return [json_path, markdown_path]


def _record_payload(record: EnrichmentRecord) -> dict[str, object]:
    selected_ratio = (
        round(record.selected_token_count / record.extracted_token_count, 4)
        if record.extracted_token_count
        else 0
    )
    return {
        **record.model_dump(mode="json"),
        "selected_token_ratio": selected_ratio,
    }


def _service_summaries(records: list[EnrichmentRecord]) -> list[dict[str, object]]:
    service_keys = sorted({record.service_key for record in records})
    summaries: list[dict[str, object]] = []
    for service_key in service_keys:
        service_records = [record for record in records if record.service_key == service_key]
        usable_count = sum(
            record.status in {EnrichmentStatus.ENRICHED, EnrichmentStatus.FALLBACK}
            for record in service_records
        )
        enriched_tokens = [
            record.extracted_token_count
            for record in service_records
            if record.status == EnrichmentStatus.ENRICHED
        ]
        summaries.append(
            {
                "service_key": service_key,
                "service_name": service_records[0].service_name,
                "candidate_count": len(service_records),
                "usable_count": usable_count,
                "usable_rate": _percentage(usable_count, len(service_records)),
                "status_counts": _count_values(record.status.value for record in service_records),
                "input_strategy_counts": _count_values(
                    record.input_strategy.value for record in service_records
                ),
                "document_type_counts": _count_values(
                    record.document_type for record in service_records if record.document_type
                ),
                "failure_reason_counts": _count_values(
                    record.failure_reason.value
                    for record in service_records
                    if record.failure_reason
                ),
                "extracted_token_distribution": _token_distribution(enriched_tokens),
            }
        )
    return summaries


def _stage_status(records: list[EnrichmentRecord], usable_count: int) -> str:
    if not records:
        return "success"
    if all(record.status == EnrichmentStatus.ENRICHED for record in records):
        return "success"
    if usable_count == 0:
        return "failed"
    return "partial"


def _is_writer_ready(record: EnrichmentRecord) -> bool:
    if record.status == EnrichmentStatus.FALLBACK:
        return record.input_strategy == EnrichmentInputStrategy.FEED_METADATA_ONLY
    return (
        record.status == EnrichmentStatus.ENRICHED
        and record.input_strategy == EnrichmentInputStrategy.FULL_CONTENT
        and record.selected_token_count > 0
    )


def _token_distribution(values: list[int]) -> dict[str, int]:
    return {
        **_value_distribution(values),
        "lte_1000": sum(value <= 1000 for value in values),
        "lte_2000": sum(value <= 2000 for value in values),
        "lte_4000": sum(value <= 4000 for value in values),
        "lte_8000": sum(value <= 8000 for value in values),
        "gt_8000": sum(value > 8000 for value in values),
    }


def _value_distribution(values: list[int]) -> dict[str, int]:
    return {
        "count": len(values),
        "p50": _percentile(values, 0.5),
        "p90": _percentile(values, 0.9),
        "max": max(values, default=0),
    }


def _percentile(values: list[int], percentile: float) -> int:
    if not values:
        return 0
    sorted_values = sorted(values)
    index = (len(sorted_values) - 1) * percentile
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return sorted_values[lower]
    interpolated = sorted_values[lower] * (upper - index) + sorted_values[upper] * (index - lower)
    return round(interpolated)


def _percentage(value: int, total: int) -> float:
    return round(value / total * 100, 1) if total else 0


def _ratio(value: int, total: int) -> float:
    return round(value / total, 4) if total else 0


def _count_values(values: Iterable[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def _format_counts(counts: dict[str, object]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in counts.items()) or "-"
