import argparse
from pathlib import Path

from src.models import ServiceCollectionResult
from src.processing.news_preprocessor import NewsPreprocessor
from src.processing.processed_writer import write_preprocessing_result
from src.processing.state.briefed_article_store import BriefedArticleStore
from src.settings import SETTINGS
from src.tracing import write_preprocessing_trace


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.processing",
        description="Preprocess collected Today in Tech raw articles into agent candidates.",
    )
    parser.add_argument(
        "--date",
        help="Target date directory in YYYY-MM-DD format. Defaults to TODAYINTECH_TARGET_DATE or today.",
    )
    parser.add_argument(
        "--raw-dir",
        default=str(SETTINGS.raw_output_dir),
        help="Raw collection root. Defaults to TODAYINTECH_RAW_OUTPUT_DIR or .var/local/raw.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(SETTINGS.processed_output_dir),
        help=(
            "Preprocessing output root. Defaults to TODAYINTECH_PROCESSED_OUTPUT_DIR "
            "or .var/local/processed."
        ),
    )
    parser.add_argument(
        "--briefed-state",
        default=str(SETTINGS.briefed_articles_path),
        help=(
            "Briefed articles state JSON path. Defaults to "
            "TODAYINTECH_BRIEFED_ARTICLES_PATH or data/briefed_articles.json."
        ),
    )
    parser.add_argument(
        "--per-service-limit",
        type=int,
        default=SETTINGS.max_candidates_per_service,
        help="Maximum candidates kept per service.",
    )
    parser.add_argument(
        "--total-limit",
        type=int,
        default=SETTINGS.max_candidates_total,
        help="Maximum candidates kept across all services.",
    )
    parser.add_argument(
        "--trace-dir",
        help="Optional trace output root. When set, writes preprocessing trace JSON and Markdown.",
    )
    return parser


def load_collection_results(raw_date_dir: Path) -> list[ServiceCollectionResult]:
    service_dir = raw_date_dir / "services"
    if not service_dir.exists():
        raise FileNotFoundError(f"Raw service directory not found: {service_dir}")

    return [
        ServiceCollectionResult.model_validate_json(path.read_text(encoding="utf-8"))
        for path in sorted(service_dir.glob("*.json"))
    ]


def print_preprocessing_report(result, written_paths: list[Path]) -> None:
    print("Preprocessing results")
    print("=====================")
    print(f"Duration: {result.duration_ms} ms")
    print(f"Raw articles: {result.raw_count}")
    print(f"Candidates: {result.candidate_count}")
    print(f"Excluded: {result.excluded_count}")
    print()

    for service in result.services:
        print(
            f"{service.service_key}: "
            f"{service.candidate_count} candidates / {service.excluded_count} excluded"
        )
        for candidate in service.candidates[:3]:
            print(f"- [{candidate.candidate_score}] {candidate.article.title}")
            print(f"  {candidate.normalized_url}")
        print()

    print("Written files")
    print("=============")
    for path in written_paths:
        print(f"- {path}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    target_date = SETTINGS.resolve_target_date(args.date)
    raw_date_dir = Path(args.raw_dir) / target_date
    collection_results = load_collection_results(raw_date_dir)
    store = BriefedArticleStore(Path(args.briefed_state))
    preprocessor = NewsPreprocessor.create_default(
        briefed_article_store=store,
        per_service_limit=max(args.per_service_limit, 1),
        total_limit=max(args.total_limit, 1),
    )
    result = preprocessor.process(target_date, collection_results)

    written_paths = write_preprocessing_result(Path(args.output_dir) / target_date, result)
    if args.trace_dir:
        written_paths.extend(write_preprocessing_trace(Path(args.trace_dir), result))

    print_preprocessing_report(result, written_paths)


if __name__ == "__main__":
    main()
