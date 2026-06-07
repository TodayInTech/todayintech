import json
import os
from datetime import UTC, datetime
from pathlib import Path

from src.models import ServiceCollectionResult


def build_collection_trace(
    generated_for: str,
    results: list[ServiceCollectionResult],
) -> dict[str, object]:
    total_duration_ms = sum(result.duration_ms for result in results)
    failed_count = sum(1 for result in results if result.status == "failed")
    warning_count = sum(len(result.warning_codes) for result in results)

    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_for": generated_for,
        "stage": "collection",
        "status": "failed" if failed_count else "success",
        "git_sha": os.getenv("GITHUB_SHA"),
        "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "service_count": len(results),
        "failed_service_count": failed_count,
        "warning_count": warning_count,
        "total_article_count": sum(len(result.articles) for result in results),
        "duration_ms": total_duration_ms,
        "services": [
            {
                "service_key": result.service_key,
                "service_name": result.service_name,
                "strategy": result.collection_method,
                "status": result.status,
                "article_count": len(result.articles),
                "duration_ms": result.duration_ms,
                "avg_article_duration_ms": round(
                    result.duration_ms / len(result.articles),
                    2,
                )
                if result.articles
                else None,
                "warning_codes": result.warning_codes,
                "error": result.error,
            }
            for result in results
        ],
    }


def build_collection_trace_markdown(trace: dict[str, object]) -> str:
    services = trace["services"]
    assert isinstance(services, list)

    lines = [
        f"# Collection Trace - {trace['generated_for']}",
        "",
        "## Summary",
        "",
        f"- Status: `{trace['status']}`",
        f"- Services: {trace['service_count']}",
        f"- Failed services: {trace['failed_service_count']}",
        f"- Warnings: {trace['warning_count']}",
        f"- Total articles: {trace['total_article_count']}",
        f"- Total duration: {trace['duration_ms']} ms",
        "",
        "## Services",
        "",
        "| Service | Strategy | Status | Articles | Duration | Warnings |",
        "| --- | --- | --- | ---: | ---: | --- |",
    ]

    for service in services:
        assert isinstance(service, dict)
        warnings = service.get("warning_codes") or []
        warning_text = ", ".join(str(warning) for warning in warnings) if warnings else "-"
        lines.append(
            "| "
            f"{service['service_key']} | "
            f"{service['strategy']} | "
            f"{service['status']} | "
            f"{service['article_count']} | "
            f"{service['duration_ms']} ms | "
            f"{warning_text} |"
        )

    lines.append("")
    return "\n".join(lines)


def write_collection_trace(
    trace_root_dir: Path,
    generated_for: str,
    results: list[ServiceCollectionResult],
) -> list[Path]:
    output_dir = trace_root_dir / generated_for
    output_dir.mkdir(parents=True, exist_ok=True)

    trace = build_collection_trace(generated_for, results)
    json_path = output_dir / "collection.json"
    markdown_path = output_dir / "summary.md"

    json_path.write_text(
        json.dumps(trace, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    markdown_path.write_text(
        build_collection_trace_markdown(trace),
        encoding="utf-8",
    )

    return [json_path, markdown_path]
