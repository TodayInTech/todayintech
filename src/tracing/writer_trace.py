from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.writer.agent.schemas import AgentDecision


def build_writer_decision_trace(
    *,
    generated_for: str,
    agent_name: str,
    decisions: list[AgentDecision],
) -> dict[str, object]:
    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_for": generated_for,
        "stage": "writer",
        "status": "success",
        "agent": agent_name,
        "git_sha": os.getenv("GITHUB_SHA"),
        "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "decision_count": len(decisions),
        "decision_counts": count_decisions(decisions),
        "decisions": [
            {
                "candidate_id": decision.candidate_id,
                "service_key": decision.service_key,
                "service_name": decision.service_name,
                "title": decision.title,
                "normalized_url": decision.normalized_url,
                "article_doc_path": decision.article_doc_path,
                "status": decision.status.value,
                "generation_method": decision.generation_method.value,
                "category": decision.category,
                "importance_level": decision.importance_level,
                "confidence_score": decision.confidence_score,
                "summary_scope": decision.summary_scope,
                "publish_reason_ko": decision.publish_reason_ko,
                "reject_reason_ko": decision.reject_reason_ko,
                "evidence_basis_ko": decision.evidence_basis_ko,
                "candidate_score": decision.candidate_score,
                "error_message": decision.error_message,
            }
            for decision in decisions
        ],
    }


def count_decisions(decisions: list[AgentDecision]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for decision in decisions:
        counts[decision.status.value] = counts.get(decision.status.value, 0) + 1
    return counts


def build_writer_decision_trace_markdown(trace: dict[str, object]) -> str:
    decisions = trace["decisions"]
    assert isinstance(decisions, list)
    decision_counts = trace["decision_counts"]
    assert isinstance(decision_counts, dict)

    lines = [
        f"# Writer Decision Trace - {trace['generated_for']}",
        "",
        "## Summary",
        "",
        f"- Status: `{trace['status']}`",
        f"- Agent: `{trace['agent']}`",
        f"- Decisions: {trace['decision_count']}",
        f"- Decision counts: {_format_counts(decision_counts)}",
        "",
        "## Decisions",
        "",
        "| Service | Decision | Score | Confidence | Title | Reason |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]

    for decision in decisions:
        assert isinstance(decision, dict)
        confidence = decision.get("confidence_score")
        reason = (
            decision.get("publish_reason_ko")
            or decision.get("reject_reason_ko")
            or decision.get("error_message")
            or "-"
        )
        lines.append(
            "| "
            f"{decision['service_key']} | "
            f"`{decision['status']}` | "
            f"{decision['candidate_score']} | "
            f"{confidence if confidence is not None else '-'} | "
            f"{_escape_table_text(str(decision['title']))} | "
            f"{_escape_table_text(str(reason))} |"
        )

    lines.append("")
    return "\n".join(lines)


def write_writer_decision_trace(
    trace_root_dir: Path,
    *,
    generated_for: str,
    agent_name: str,
    decisions: list[AgentDecision],
) -> list[Path]:
    output_dir = trace_root_dir / generated_for
    output_dir.mkdir(parents=True, exist_ok=True)

    trace = build_writer_decision_trace(
        generated_for=generated_for,
        agent_name=agent_name,
        decisions=decisions,
    )
    json_path = output_dir / "writer-decisions.json"
    markdown_path = output_dir / "writer-decisions-summary.md"

    json_path.write_text(
        json.dumps(trace, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    markdown_path.write_text(
        build_writer_decision_trace_markdown(trace),
        encoding="utf-8",
    )

    return [json_path, markdown_path]


def _format_counts(counts: dict[str, object]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in sorted(counts.items())) or "-"


def _escape_table_text(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
