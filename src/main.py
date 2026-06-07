from src.collection import NewsCollector, write_raw_collection_results
from src.generator.service_markdown_writer import write_service_markdown
from src.generator.summary_markdown_writer import write_summary_markdown
from src.models import BriefingBundle, ServiceBriefing
from src.processing.deduplicator import deduplicate_articles
from src.processing.summarizer import summarize_article
from src.settings import SETTINGS
from src.sources import NewsSourceFactory


def run_pipeline(target_date: str | None = None) -> BriefingBundle:
    generated_for = SETTINGS.resolve_target_date(target_date)
    max_articles = SETTINGS.max_articles_per_service

    source_factory = NewsSourceFactory()
    collector = NewsCollector(source_factory)
    collection_results = collector.collect_all()
    write_raw_collection_results(SETTINGS.raw_output_dir / generated_for, collection_results)

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

    output_dir = SETTINGS.output_dir / generated_for
    for briefing in service_briefings:
        write_service_markdown(output_dir, briefing)
    write_summary_markdown(output_dir, bundle)

    return bundle


def main() -> None:
    bundle = run_pipeline()
    print(f"Generated briefing bundle for {bundle.generated_for}")


if __name__ == "__main__":
    main()
