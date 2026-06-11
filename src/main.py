from src.collection import NewsCollector, write_raw_collection_results
from src.generator.service_markdown_writer import write_service_markdown
from src.generator.summary_markdown_writer import write_summary_markdown
from src.models import BriefingBundle, ServiceBriefing
from src.processing import BriefedArticleStore, NewsPreprocessor
from src.processing.processed_writer import write_preprocessing_result
from src.processing.summarizer import summarize_article
from src.settings import SETTINGS
from src.sources import NewsSourceFactory


def run_pipeline(target_date: str | None = None) -> BriefingBundle:
    generated_for = SETTINGS.resolve_target_date(target_date)
    max_articles = SETTINGS.max_articles_per_service

    source_factory = NewsSourceFactory()
    collector = NewsCollector(source_factory)

    # 1. Collector 단계: 외부 source에서 오늘 기준 raw snapshot을 수집하고 저장한다.
    collection_results = collector.collect_all()
    write_raw_collection_results(SETTINGS.raw_output_dir / generated_for, collection_results)

    # 2. Preprocessor 단계: raw snapshot을 Agent 입력 후보로 정리하고 저장한다.
    briefed_article_store = BriefedArticleStore(SETTINGS.briefed_articles_path)
    preprocessor = NewsPreprocessor.create_default(
        briefed_article_store=briefed_article_store,
        per_service_limit=SETTINGS.max_candidates_per_service,
        total_limit=SETTINGS.max_candidates_total,
    )
    preprocessing_result = preprocessor.process(generated_for, collection_results)
    write_preprocessing_result(
        SETTINGS.processed_output_dir / generated_for,
        preprocessing_result,
    )

    # 3. Generator 단계: 현재는 legacy Markdown scaffold를 전처리 후보 기준으로 생성한다.
    #    article archive generator가 구현되면 이 구간을 글 단위 문서 생성으로 교체한다.
    service_briefings: list[ServiceBriefing] = []
    for result in preprocessing_result.services:
        candidates = result.candidates[:max_articles]
        summaries = [summarize_article(candidate.article) for candidate in candidates]
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
