import json
from datetime import UTC, datetime
from pathlib import Path

from src.models import ServiceCollectionResult


def write_raw_collection_results(
    output_dir: Path,
    results: list[ServiceCollectionResult],
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    service_dir = output_dir / "services"
    service_dir.mkdir(parents=True, exist_ok=True)

    written_paths: list[Path] = []
    summary = []

    for result in results:
        service_path = service_dir / f"{result.service_key}.json"
        service_path.write_text(
            json.dumps(result.model_dump(mode="json"), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        written_paths.append(service_path)
        summary.append(
            {
                "service_key": result.service_key,
                "service_name": result.service_name,
                "source_url": result.source_url,
                "collection_method": result.collection_method,
                "status": result.status,
                "article_count": len(result.articles),
                "error": result.error,
            }
        )

    summary_path = output_dir / "summary.json"
    summary_path.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(UTC).isoformat(),
                "services": summary,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    written_paths.append(summary_path)

    return written_paths
