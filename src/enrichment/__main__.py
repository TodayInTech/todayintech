import argparse
from pathlib import Path

from src.enrichment.content_enricher import ContentEnricher
from src.enrichment.storage import write_enrichment_result
from src.processing.models import PreprocessingResult
from src.settings import SETTINGS
from src.tracing import write_enrichment_trace


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.enrichment",
        description="Fetch and structure source evidence for preprocessed candidates.",
    )
    parser.add_argument("--date", help="Target date in YYYY-MM-DD format.")
    parser.add_argument(
        "--processed-dir",
        default=str(SETTINGS.processed_output_dir),
        help="Preprocessing output root.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(SETTINGS.enriched_output_dir),
        help="Enrichment output root.",
    )
    parser.add_argument(
        "--cache-dir",
        default=str(SETTINGS.enrichment_cache_dir),
        help="Enrichment cache root.",
    )
    parser.add_argument(
        "--trace-dir",
        help="Optional trace output root.",
    )
    return parser


def load_preprocessing_result(processed_date_dir: Path) -> PreprocessingResult:
    input_path = processed_date_dir / "preprocessing.json"
    if not input_path.exists():
        raise FileNotFoundError(f"Preprocessing result not found: {input_path}")
    return PreprocessingResult.model_validate_json(input_path.read_text(encoding="utf-8"))


def main() -> None:
    args = build_parser().parse_args()
    target_date = SETTINGS.resolve_target_date(args.date)
    preprocessing_result = load_preprocessing_result(Path(args.processed_dir) / target_date)
    enricher = ContentEnricher.create_default(
        cache_dir=Path(args.cache_dir),
        timeout_seconds=SETTINGS.enrichment_timeout_seconds,
        max_attempts=SETTINGS.enrichment_max_attempts,
        minimum_tokens=SETTINGS.enrichment_minimum_tokens,
        full_content_max_tokens=SETTINGS.enrichment_full_content_max_tokens,
        chunk_selection_max_tokens=SETTINGS.enrichment_chunk_selection_max_tokens,
        chunk_max_tokens=SETTINGS.enrichment_chunk_max_tokens,
        selected_chunks_max_tokens=SETTINGS.enrichment_selected_chunks_max_tokens,
    )
    result = enricher.enrich(preprocessing_result)
    written_paths = write_enrichment_result(
        Path(args.output_dir) / target_date,
        result,
    )
    if args.trace_dir:
        written_paths.extend(write_enrichment_trace(Path(args.trace_dir), result))

    print("Enrichment results")
    print("==================")
    print(f"Candidates: {len(result.candidates)}")
    print(
        "Usable: "
        f"{sum(candidate.status.value in {'enriched', 'fallback'} for candidate in result.candidates)}"
    )
    print(f"Duration: {result.duration_ms} ms")
    for path in written_paths:
        print(f"- {path}")


if __name__ == "__main__":
    main()
