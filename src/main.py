import os
from datetime import UTC, datetime
from pathlib import Path

from src.collection import NewsCollector, write_raw_collection_results
from src.generator.service_markdown_writer import write_service_markdown
from src.generator.summary_markdown_writer import write_summary_markdown
from src.models import BriefingBundle, ServiceBriefing
from src.processing.deduplicator import deduplicate_articles
from src.processing.summarizer import summarize_article
from src.sources import NewsSourceFactory


def get_target_date(target_date: str | None = None) -> str:
    return (
        target_date or os.getenv("TODAYINTECH_TARGET_DATE") or datetime.now(UTC).date().isoformat()
    )


def get_max_articles_per_service() -> int:
    value = os.getenv("TODAYINTECH_MAX_ARTICLES_PER_SERVICE", "5")
    try:
        return max(1, int(value))
    except ValueError:
        return 5


def run_pipeline(target_date: str | None = None) -> BriefingBundle:
    generated_for = get_target_date(target_date)
    max_articles = get_max_articles_per_service()
    docs_output_dir = Path(os.getenv("TODAYINTECH_OUTPUT_DIR", "docs"))
    raw_output_dir = Path(os.getenv("TODAYINTECH_RAW_OUTPUT_DIR", "data/raw"))

    source_factory = NewsSourceFactory()
    collector = NewsCollector(source_factory)
    collection_results = collector.collect_all()
    write_raw_collection_results(raw_output_dir / generated_for, collection_results)

    service_briefings: list[ServiceBriefing] = []

    for result in collection_results:
        articles = deduplicate_articles(result.articles)
        summaries = [summarize_article(article) for article in articles[:max_articles]]
        service_briefings.append(
            ServiceBriefing(
                service_key=result.service_key,
                service_name=result.service_name,
                generated_for=generated_for,
                summaries=summaries,
            )
        )

    bundle = BriefingBundle(
        generated_for=generated_for,
        service_briefings=service_briefings,
        insight_ko="서비스별 주요 기술 뉴스를 수집하고 도메인별로 묶은 자동 브리핑입니다.",
    )

    output_dir = docs_output_dir / generated_for
    for briefing in service_briefings:
        write_service_markdown(output_dir, briefing)
    write_summary_markdown(output_dir, bundle)

    return bundle


def main() -> None:
    bundle = run_pipeline()
    print(f"Generated briefing bundle for {bundle.generated_for}")


if __name__ == "__main__":
    main()
