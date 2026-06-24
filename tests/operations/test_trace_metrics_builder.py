import json
from pathlib import Path

from src.operations.trace_metrics_builder import build_trace_metrics


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_build_trace_metrics_uses_remote_trace_history_only(tmp_path) -> None:
    trace_history_dir = tmp_path / "tracing-history"
    date_dir = trace_history_dir / "traces" / "2026-06-24"
    write_json(
        date_dir / "collection.json",
        {
            "generated_for": "2026-06-24",
            "status": "success",
            "git_sha": "abc123456",
            "github_run_id": "1234",
            "service_count": 1,
            "failed_service_count": 0,
            "warning_count": 0,
            "total_article_count": 20,
            "duration_ms": 100,
            "services": [
                {
                    "service_key": "hacker-news",
                    "service_name": "Hacker News",
                    "strategy": "rss",
                    "status": "success",
                    "article_count": 20,
                    "duration_ms": 80,
                    "warning_codes": [],
                }
            ],
        },
    )
    write_json(
        date_dir / "preprocessing.json",
        {
            "generated_for": "2026-06-24",
            "status": "success",
            "raw_count": 20,
            "candidate_count": 4,
            "excluded_count": 16,
            "duration_ms": 10,
            "step_metrics": [
                {
                    "step_name": "briefed_article_filter",
                    "reason_counts": {"already_briefed": 10},
                },
                {
                    "step_name": "candidate_quality_gate",
                    "reason_counts": {"low_quality": 6},
                },
            ],
            "services": [
                {
                    "service_key": "hacker-news",
                    "service_name": "Hacker News",
                    "raw_count": 20,
                    "candidate_count": 4,
                    "excluded_count": 16,
                    "excluded_reasons": {"already_briefed": 10, "low_quality": 6},
                }
            ],
        },
    )
    write_json(
        date_dir / "enrichment.json",
        {
            "generated_for": "2026-06-24",
            "status": "partial",
            "candidate_count": 4,
            "usable_count": 3,
            "status_counts": {"enriched": 2, "fallback": 1, "failed": 1},
            "input_strategy_counts": {"chunk_selection": 1, "feed_metadata_only": 1},
            "failure_reason_counts": {"thin_content": 1},
            "services": [
                {
                    "service_key": "hacker-news",
                    "service_name": "Hacker News",
                    "candidate_count": 4,
                    "usable_count": 3,
                    "status_counts": {"enriched": 2, "fallback": 1, "failed": 1},
                    "input_strategy_counts": {
                        "chunk_selection": 1,
                        "feed_metadata_only": 1,
                    },
                    "failure_reason_counts": {"thin_content": 1},
                }
            ],
            "records": [
                {
                    "service_key": "hacker-news",
                    "status": "enriched",
                    "input_strategy": "chunk_selection",
                    "selected_token_count": 1800,
                    "selected_chunk_count": 2,
                },
                {
                    "service_key": "hacker-news",
                    "status": "fallback",
                    "input_strategy": "feed_metadata_only",
                    "selected_token_count": 0,
                    "selected_chunk_count": 0,
                },
                {
                    "service_key": "hacker-news",
                    "status": "failed",
                    "input_strategy": "none",
                    "selected_token_count": 0,
                    "selected_chunk_count": 0,
                },
            ],
        },
    )
    write_json(
        date_dir / "writer-decisions.json",
        {
            "generated_for": "2026-06-24",
            "status": "success",
            "agent": "openai",
            "decision_count": 2,
            "decision_counts": {"published": 1, "skipped": 1},
            "decisions": [
                {
                    "service_key": "hacker-news",
                    "service_name": "Hacker News",
                    "status": "published",
                    "summary_scope": "chunk_selection",
                    "confidence_score": 0.82,
                },
                {
                    "service_key": "hacker-news",
                    "service_name": "Hacker News",
                    "status": "skipped",
                    "summary_scope": "feed_metadata_only",
                    "confidence_score": 0.61,
                },
            ],
        },
    )

    metrics = build_trace_metrics(trace_history_dir)

    assert metrics["source"] == "tracing-history"
    assert metrics["date_range"] == {"start": "2026-06-24", "end": "2026-06-24"}
    assert metrics["service_names"] == {"hacker-news": "Hacker News"}
    assert metrics["runs"][0]["collection"]["total_article_count"] == 20
    assert metrics["runs"][0]["preprocessing"]["candidate_rate"] == 20.0
    assert metrics["runs"][0]["enrichment"]["writer_ready_count"] == 2
    assert metrics["runs"][0]["writer"]["publish_rate"] == 50.0
    assert metrics["services"][0]["enrichment"]["writer_ready_count"] == 2
    assert metrics["services"][0]["writer"]["summary_scope_counts"] == {
        "chunk_selection": 1,
        "feed_metadata_only": 1,
    }
