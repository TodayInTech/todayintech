import json
from pathlib import Path


def write_operations_data(output_dir: Path, metrics: dict[str, object]) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "trace-metrics.json"
    output_path.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path
