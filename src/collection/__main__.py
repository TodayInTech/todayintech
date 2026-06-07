import argparse
from pathlib import Path

from src.collection import NewsCollector, write_raw_collection_results
from src.models import Article, ServiceCollectionResult
from src.settings import SETTINGS
from src.sources import NewsSourceFactory
from src.tracing import write_collection_trace


def build_parser(service_keys: tuple[str, ...]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.collection",
        description="Collect Today in Tech source data and write service-level raw JSON.",
    )
    parser.add_argument(
        "--service",
        choices=service_keys,
        help="Collect only one service. Collects every registered service when omitted.",
    )
    parser.add_argument(
        "--date",
        help="Target date directory in YYYY-MM-DD format. Defaults to TODAYINTECH_TARGET_DATE or today.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(SETTINGS.raw_output_dir),
        help="Raw collection output root. Defaults to TODAYINTECH_RAW_OUTPUT_DIR or data/raw.",
    )
    parser.add_argument(
        "--preview-limit",
        type=int,
        default=3,
        help="Number of collected articles to print per service. Use 0 to hide previews.",
    )
    parser.add_argument(
        "--trace-dir",
        help="Optional trace output root. When set, writes collection trace JSON and Markdown.",
    )
    return parser


def collect_results(
    collector: NewsCollector,
    service_key: str | None,
) -> list[ServiceCollectionResult]:
    if service_key is None:
        return collector.collect_all()
    return [collector.collect_by_service_key(service_key)]


def format_article_preview(article: Article) -> str:
    published_at = article.published_at.date().isoformat() if article.published_at else "no-date"
    return f"- [{published_at}] {article.title}\n  {article.url}"


def print_collection_report(
    results: list[ServiceCollectionResult],
    written_paths: list[Path],
    preview_limit: int,
) -> None:
    print("Collection results")
    print("==================")

    for result in results:
        print(
            f"{result.service_key}: {result.status} "
            f"({len(result.articles)} articles, {result.collection_method})"
        )
        if result.error:
            print(f"  error: {result.error}")
            continue

        for article in result.articles[: max(0, preview_limit)]:
            print(format_article_preview(article))
        if preview_limit > 0 and len(result.articles) > preview_limit:
            hidden_count = len(result.articles) - preview_limit
            print(f"  ... {hidden_count} more articles")
        print()

    print("Written files")
    print("=============")
    for path in written_paths:
        print(f"- {path}")


def main() -> None:
    source_factory = NewsSourceFactory()
    parser = build_parser(source_factory.service_keys())
    args = parser.parse_args()

    target_date = SETTINGS.resolve_target_date(args.date)
    output_dir = Path(args.output_dir) / target_date
    collector = NewsCollector(source_factory)
    results = collect_results(collector, args.service)
    written_paths = write_raw_collection_results(output_dir, results)
    if args.trace_dir:
        written_paths.extend(write_collection_trace(Path(args.trace_dir), target_date, results))

    print_collection_report(results, written_paths, args.preview_limit)

    if any(result.status == "failed" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
