import json
from pathlib import Path

from src.enrichment.models import EnrichmentResult


def write_enrichment_result(output_dir: Path, result: EnrichmentResult) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "enrichment.json"
    output_path.write_text(
        json.dumps(result.model_dump(mode="json"), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return [output_path]
