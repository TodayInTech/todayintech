from datetime import UTC, datetime
from pathlib import Path

from src.generator.service_markdown_writer import write_service_markdown
from src.generator.summary_markdown_writer import write_summary_markdown
from src.models import BriefingBundle, ServiceBriefing
from src.processing.deduplicator import deduplicate_articles
from src.processing.summarizer import summarize_article
from src.services import NewsServiceFactory


def run_pipeline(target_date: str | None = None) -> BriefingBundle:
    generated_for = target_date or datetime.now(UTC).date().isoformat()
    factory = NewsServiceFactory()
    service_briefings: list[ServiceBriefing] = []

    for service in factory.create_all():
        articles = deduplicate_articles(service.collect())
        summaries = [summarize_article(article) for article in articles[:5]]
        service_briefings.append(
            ServiceBriefing(
                service_key=service.service_key,
                service_name=service.service_name,
                generated_for=generated_for,
                summaries=summaries,
            )
        )

    bundle = BriefingBundle(
        generated_for=generated_for,
        service_briefings=service_briefings,
        insight_ko="서비스별 주요 기술 뉴스를 수집하고 도메인별로 묶은 자동 브리핑입니다.",
    )

    output_dir = Path("docs") / generated_for
    for briefing in service_briefings:
        write_service_markdown(output_dir, briefing)
    write_summary_markdown(output_dir, bundle)

    return bundle


def main() -> None:
    bundle = run_pipeline()
    print(f"Generated briefing bundle for {bundle.generated_for}")
