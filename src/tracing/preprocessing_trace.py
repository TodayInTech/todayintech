import json
import os
from datetime import UTC, datetime
from pathlib import Path

from src.processing.models import PreprocessingResult


def build_preprocessing_trace(result: PreprocessingResult) -> dict[str, object]:
    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_for": result.generated_for,
        "stage": "preprocessing",
        "status": "success",
        "git_sha": os.getenv("GITHUB_SHA"),
        "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "service_count": len(result.services),
        "duration_ms": result.duration_ms,
        "raw_count": result.raw_count,
        "candidate_count": result.candidate_count,
        "excluded_count": result.excluded_count,
        "step_metrics": [
            {
                "step_name": metrics.step_name,
                "input_count": metrics.input_count,
                "output_count": metrics.output_count,
                "excluded_count": metrics.excluded_count,
                "duration_ms": metrics.duration_ms,
                "reason_counts": {
                    reason.value: count for reason, count in metrics.reason_counts.items()
                },
            }
            for metrics in result.step_metrics
        ],
        "services": [
            {
                "service_key": service.service_key,
                "service_name": service.service_name,
                "raw_count": service.raw_count,
                "candidate_count": service.candidate_count,
                "excluded_count": service.excluded_count,
                "top_candidates": [
                    {
                        "candidate_id": candidate.candidate_id,
                        "title": candidate.article.title,
                        "normalized_url": candidate.normalized_url,
                        "url_hash": candidate.url_hash,
                        "suggested_doc_key": candidate.suggested_doc_key,
                        "suggested_article_path": candidate.suggested_article_path,
                        "candidate_score": candidate.candidate_score,
                        "ranking_reasons_ko": candidate.ranking_reasons_ko,
                    }
                    for candidate in service.candidates[:5]
                ],
                "excluded_reasons": count_excluded_reasons(service),
            }
            for service in result.services
        ],
    }


def count_excluded_reasons(service) -> dict[str, int]:
    counts: dict[str, int] = {}
    for candidate in service.excluded:
        reason = candidate.excluded_reason.value if candidate.excluded_reason else "unknown"
        counts[reason] = counts.get(reason, 0) + 1
    return counts


def build_preprocessing_trace_markdown(trace: dict[str, object]) -> str:
    services = trace["services"]
    assert isinstance(services, list)

    lines = [
        f"# Preprocessing Trace - {trace['generated_for']}",
        "",
        "## Summary",
        "",
        f"- Status: `{trace['status']}`",
        f"- Services: {trace['service_count']}",
        f"- Duration: {trace['duration_ms']} ms",
        f"- Raw articles: {trace['raw_count']}",
        f"- Candidates: {trace['candidate_count']}",
        f"- Excluded: {trace['excluded_count']}",
        "",
        "## Services",
        "",
        "| Service | Raw | Candidates | Excluded | Excluded reasons |",
        "| --- | ---: | ---: | ---: | --- |",
    ]

    for service in services:
        assert isinstance(service, dict)
        reasons = service.get("excluded_reasons") or {}
        assert isinstance(reasons, dict)
        reason_text = ", ".join(f"{key}: {value}" for key, value in reasons.items()) or "-"
        lines.append(
            "| "
            f"{service['service_key']} | "
            f"{service['raw_count']} | "
            f"{service['candidate_count']} | "
            f"{service['excluded_count']} | "
            f"{reason_text} |"
        )

    lines.append("")
    return "\n".join(lines)


def write_preprocessing_trace(
    trace_root_dir: Path,
    result: PreprocessingResult,
) -> list[Path]:
    output_dir = trace_root_dir / result.generated_for
    output_dir.mkdir(parents=True, exist_ok=True)

    trace = build_preprocessing_trace(result)
    json_path = output_dir / "preprocessing.json"
    markdown_path = output_dir / "preprocessing-summary.md"

    json_path.write_text(
        json.dumps(trace, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    markdown_path.write_text(
        build_preprocessing_trace_markdown(trace),
        encoding="utf-8",
    )

    return [json_path, markdown_path]
