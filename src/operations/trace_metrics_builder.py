from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from src.operations.trace_history_reader import read_trace_history

SERVICE_ORDER = [
    "hacker-news",
    "github-blog",
    "google-blog",
    "openai-blog",
    "anthropic-blog",
]


def build_trace_metrics(trace_history_dir: Path) -> dict[str, object]:
    trace_runs = read_trace_history(trace_history_dir)
    runs = [_run_summary(trace_run) for trace_run in trace_runs]
    services = [
        service_summary
        for trace_run in trace_runs
        for service_summary in _service_summaries(trace_run)
    ]
    service_names = _service_names(services)

    dates = [run["date"] for run in runs]
    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "source": "tracing-history",
        "date_range": {
            "start": min(dates) if dates else None,
            "end": max(dates) if dates else None,
        },
        "service_names": service_names,
        "runs": runs,
        "services": services,
    }


def _run_summary(trace_run: dict[str, Any]) -> dict[str, Any]:
    collection = trace_run.get("collection") or {}
    preprocessing = trace_run.get("preprocessing") or {}
    enrichment = trace_run.get("enrichment") or {}
    writer = trace_run.get("writer") or {}
    github_run_id = (
        collection.get("github_run_id")
        or preprocessing.get("github_run_id")
        or enrichment.get("github_run_id")
        or writer.get("github_run_id")
    )
    git_sha = (
        collection.get("git_sha")
        or preprocessing.get("git_sha")
        or enrichment.get("git_sha")
        or writer.get("git_sha")
    )
    writer_decision_counts = _dict(writer.get("decision_counts"))
    return {
        "date": trace_run["date"],
        "github_run_id": github_run_id,
        "git_sha": git_sha,
        "status": _combined_status(
            collection.get("status"),
            preprocessing.get("status"),
            enrichment.get("status"),
            writer.get("status"),
        ),
        "collection": {
            "available": bool(collection),
            "status": collection.get("status"),
            "service_count": _int(collection.get("service_count")),
            "failed_service_count": _int(collection.get("failed_service_count")),
            "warning_count": _int(collection.get("warning_count")),
            "total_article_count": _int(collection.get("total_article_count")),
            "duration_ms": _int(collection.get("duration_ms")),
        },
        "preprocessing": {
            "available": bool(preprocessing),
            "status": preprocessing.get("status"),
            "raw_count": _int(preprocessing.get("raw_count")),
            "candidate_count": _int(preprocessing.get("candidate_count")),
            "excluded_count": _int(preprocessing.get("excluded_count")),
            "candidate_rate": _percentage(
                _int(preprocessing.get("candidate_count")),
                _int(preprocessing.get("raw_count")),
            ),
            "duration_ms": _int(preprocessing.get("duration_ms")),
            "excluded_reason_counts": _step_reason_counts(preprocessing),
        },
        "enrichment": _enrichment_summary(enrichment),
        "writer": {
            "available": bool(writer),
            "status": writer.get("status"),
            "agent": writer.get("agent"),
            "decision_count": _int(writer.get("decision_count")),
            "decision_counts": writer_decision_counts,
            "published_count": _int(writer_decision_counts.get("published")),
            "skipped_count": _int(writer_decision_counts.get("skipped")),
            "failed_count": _int(writer_decision_counts.get("failed")),
            "publish_rate": _percentage(
                _int(writer_decision_counts.get("published")),
                _int(writer.get("decision_count")),
            ),
            "summary_scope_counts": _count_from_records(
                _list(writer.get("decisions")),
                "summary_scope",
            ),
            "confidence_buckets": _confidence_buckets(_list(writer.get("decisions"))),
        },
    }


def _service_summaries(trace_run: dict[str, Any]) -> list[dict[str, Any]]:
    service_map: dict[str, dict[str, Any]] = {}
    date = trace_run["date"]

    for service in _list((trace_run.get("collection") or {}).get("services")):
        service_key = service.get("service_key")
        if not service_key:
            continue
        item = _service_item(service_map, date, service_key, service.get("service_name"))
        item["collection"] = {
            "available": True,
            "status": service.get("status"),
            "strategy": service.get("strategy"),
            "article_count": _int(service.get("article_count")),
            "duration_ms": _int(service.get("duration_ms")),
            "warning_count": len(_list(service.get("warning_codes"))),
        }

    for service in _list((trace_run.get("preprocessing") or {}).get("services")):
        service_key = service.get("service_key")
        if not service_key:
            continue
        item = _service_item(service_map, date, service_key, service.get("service_name"))
        raw_count = _int(service.get("raw_count"))
        candidate_count = _int(service.get("candidate_count"))
        item["preprocessing"] = {
            "available": True,
            "raw_count": raw_count,
            "candidate_count": candidate_count,
            "excluded_count": _int(service.get("excluded_count")),
            "candidate_rate": _percentage(candidate_count, raw_count),
            "excluded_reason_counts": _dict(service.get("excluded_reasons")),
        }

    enrichment = trace_run.get("enrichment") or {}
    for service in _list(enrichment.get("services")):
        service_key = service.get("service_key")
        if not service_key:
            continue
        item = _service_item(service_map, date, service_key, service.get("service_name"))
        service_records = [
            record
            for record in _list(enrichment.get("records"))
            if record.get("service_key") == service_key
        ]
        writer_ready_count = _writer_ready_count(service_records)
        candidate_count = _int(service.get("candidate_count"))
        item["enrichment"] = {
            "available": True,
            "candidate_count": candidate_count,
            "usable_count": _int(service.get("usable_count")),
            "writer_ready_count": writer_ready_count,
            "writer_ready_rate": _percentage(writer_ready_count, candidate_count),
            "status_counts": _dict(service.get("status_counts")),
            "strategy_counts": _dict(service.get("input_strategy_counts")),
            "failure_reason_counts": _dict(service.get("failure_reason_counts")),
            "token_distribution": _dict(service.get("extracted_token_distribution")),
            "selected_token_count": sum(
                _int(record.get("selected_token_count")) for record in service_records
            ),
            "selected_chunk_count": sum(
                _int(record.get("selected_chunk_count")) for record in service_records
            ),
        }

    writer_decisions = _list((trace_run.get("writer") or {}).get("decisions"))
    for service_key, decisions in _group_by(writer_decisions, "service_key").items():
        if not service_key:
            continue
        service_name = decisions[0].get("service_name") if decisions else None
        item = _service_item(service_map, date, service_key, service_name)
        decision_counts = _count_from_records(decisions, "status")
        decision_count = len(decisions)
        item["writer"] = {
            "available": True,
            "decision_count": decision_count,
            "decision_counts": decision_counts,
            "published_count": _int(decision_counts.get("published")),
            "skipped_count": _int(decision_counts.get("skipped")),
            "failed_count": _int(decision_counts.get("failed")),
            "publish_rate": _percentage(_int(decision_counts.get("published")), decision_count),
            "summary_scope_counts": _count_from_records(decisions, "summary_scope"),
            "confidence_buckets": _confidence_buckets(decisions),
        }

    return [
        service_map[key]
        for key in sorted(
            service_map,
            key=lambda value: (
                SERVICE_ORDER.index(value) if value in SERVICE_ORDER else len(SERVICE_ORDER),
                value,
            ),
        )
    ]


def _service_item(
    service_map: dict[str, dict[str, Any]],
    date: str,
    service_key: str,
    service_name: str | None,
) -> dict[str, Any]:
    if service_key not in service_map:
        service_map[service_key] = {
            "date": date,
            "service_key": service_key,
            "service_name": service_name or service_key,
            "collection": {"available": False},
            "preprocessing": {"available": False},
            "enrichment": {"available": False},
            "writer": {"available": False},
        }
    elif service_name:
        service_map[service_key]["service_name"] = service_name
    return service_map[service_key]


def _enrichment_summary(enrichment: dict[str, Any]) -> dict[str, Any]:
    records = _list(enrichment.get("records"))
    writer_ready_count = _writer_ready_count(records)
    candidate_count = _int(enrichment.get("candidate_count"))
    return {
        "available": bool(enrichment),
        "status": enrichment.get("status"),
        "candidate_count": candidate_count,
        "usable_count": _int(enrichment.get("usable_count")),
        "writer_ready_count": writer_ready_count,
        "writer_ready_rate": _percentage(writer_ready_count, candidate_count),
        "cache_hit_count": _int(enrichment.get("cache_hit_count")),
        "cache_hit_rate": _number(enrichment.get("cache_hit_rate")),
        "status_counts": _dict(enrichment.get("status_counts")),
        "strategy_counts": _dict(enrichment.get("input_strategy_counts")),
        "failure_reason_counts": _dict(enrichment.get("failure_reason_counts")),
        "token_distribution": _dict(enrichment.get("extracted_token_distribution")),
        "selected_token_count": sum(_int(record.get("selected_token_count")) for record in records),
        "selected_chunk_count": sum(_int(record.get("selected_chunk_count")) for record in records),
        "duration_ms": _int(enrichment.get("duration_ms")),
    }


def _writer_ready_count(records: list[dict[str, Any]]) -> int:
    count = 0
    for record in records:
        status = record.get("status")
        strategy = record.get("input_strategy")
        selected_tokens = _int(record.get("selected_token_count"))
        if (status == "fallback" and strategy == "feed_metadata_only") or (
            status == "enriched" and selected_tokens > 0
        ):
            count += 1
    return count


def _step_reason_counts(preprocessing: dict[str, Any]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for step in _list(preprocessing.get("step_metrics")):
        counts.update({key: _int(value) for key, value in _dict(step.get("reason_counts")).items()})
    return dict(sorted(counts.items()))


def _combined_status(*statuses: object) -> str:
    available = [status for status in statuses if status]
    if not available:
        return "missing"
    if any(status == "failed" for status in available):
        return "failed"
    if any(status == "partial" for status in available):
        return "partial"
    return "success"


def _service_names(services: list[dict[str, Any]]) -> dict[str, str]:
    names = {
        service["service_key"]: service["service_name"]
        for service in services
        if service.get("service_key") and service.get("service_name")
    }
    return dict(sorted(names.items()))


def _group_by(records: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    grouped: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        value = record.get(key)
        if value is not None:
            grouped[str(value)].append(record)
    return grouped


def _count_from_records(records: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts = Counter(str(record[key]) for record in records if record.get(key) is not None)
    return dict(sorted(counts.items()))


def _confidence_buckets(records: list[dict[str, Any]]) -> dict[str, int]:
    buckets = {"lt_0_5": 0, "0_5_to_0_7": 0, "0_7_to_0_9": 0, "gte_0_9": 0}
    for record in records:
        confidence = record.get("confidence_score")
        if not isinstance(confidence, int | float):
            continue
        if confidence < 0.5:
            buckets["lt_0_5"] += 1
        elif confidence < 0.7:
            buckets["0_5_to_0_7"] += 1
        elif confidence < 0.9:
            buckets["0_7_to_0_9"] += 1
        else:
            buckets["gte_0_9"] += 1
    return buckets


def _percentage(value: int, total: int) -> float:
    if total <= 0:
        return 0
    return round(value / total * 100, 2)


def _int(value: object) -> int:
    return value if isinstance(value, int) else 0


def _number(value: object) -> int | float:
    return value if isinstance(value, int | float) else 0


def _dict(value: object) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _list(value: object) -> list[dict[str, Any]]:
    return value if isinstance(value, list) else []
