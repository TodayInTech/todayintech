import json
from pathlib import Path
from typing import Any

TRACE_FILE_NAMES = {
    "collection": "collection.json",
    "preprocessing": "preprocessing.json",
    "enrichment": "enrichment.json",
    "writer": "writer-decisions.json",
}


def read_trace_history(trace_history_dir: Path) -> list[dict[str, Any]]:
    traces_dir = trace_history_dir / "traces"
    if not traces_dir.exists():
        return []

    runs: list[dict[str, Any]] = []
    for date_dir in sorted(path for path in traces_dir.iterdir() if path.is_dir()):
        stages = {
            stage: _read_json(date_dir / file_name) for stage, file_name in TRACE_FILE_NAMES.items()
        }
        if any(value is not None for value in stages.values()):
            runs.append({"date": date_dir.name, **stages})
    return runs


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError, ValueError:
        return None
    return value if isinstance(value, dict) else None
