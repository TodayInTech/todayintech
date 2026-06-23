from src.collection import NewsCollector, write_raw_collection_results
from src.enrichment.content_enricher import ContentEnricher
from src.enrichment.storage import write_enrichment_result
from src.processing import BriefedArticleStore, NewsPreprocessor
from src.processing.processed_writer import write_preprocessing_result
from src.progress import log_info, log_step
from src.settings import SETTINGS
from src.sources import NewsSourceFactory
from src.tracing import write_enrichment_trace
from src.writer import NewsWriter, WriterResult
from src.writer.agent.factory import create_news_editor_agent


def run_pipeline(target_date: str | None = None) -> WriterResult:
    generated_for = SETTINGS.resolve_target_date(target_date)
    log_info("Pipeline", f"target_date={generated_for}, writer_agent={SETTINGS.writer_agent}")

    source_factory = NewsSourceFactory()
    collector = NewsCollector(source_factory)

    # 1. Collector 단계: 외부 source에서 오늘 기준 raw snapshot을 수집하고 저장한다.
    log_step(1, 4, "Collector", "서비스별 source snapshot 수집 시작")
    collection_results = collector.collect_all()
    raw_paths = write_raw_collection_results(
        SETTINGS.raw_output_dir / generated_for, collection_results
    )
    collected_articles = sum(len(result.articles) for result in collection_results)
    log_step(
        1,
        4,
        "Collector",
        f"완료: services={len(collection_results)}, articles={collected_articles}, files={len(raw_paths)}",
    )

    # 2. Preprocessor 단계: raw snapshot을 Agent 입력 후보로 정리하고 저장한다.
    log_step(2, 4, "Preprocessor", "중복 제거 및 Writer 후보 생성 시작")
    briefed_article_store = BriefedArticleStore(SETTINGS.briefed_articles_path)
    preprocessor = NewsPreprocessor.create_default(
        briefed_article_store=briefed_article_store,
        per_service_limit=SETTINGS.max_candidates_per_service,
        total_limit=SETTINGS.max_candidates_total,
    )
    preprocessing_result = preprocessor.process(generated_for, collection_results)
    processed_paths = write_preprocessing_result(
        SETTINGS.processed_output_dir / generated_for,
        preprocessing_result,
    )
    log_step(
        2,
        4,
        "Preprocessor",
        (
            "완료: "
            f"raw={preprocessing_result.raw_count}, "
            f"candidates={preprocessing_result.candidate_count}, "
            f"excluded={preprocessing_result.excluded_count}, "
            f"files={len(processed_paths)}"
        ),
    )

    # 3. Enrichment 단계: 제한된 후보의 원문 근거와 Agent 입력 전략을 준비한다.
    log_step(3, 4, "Enrichment", "후보 원문 fetch 및 구조 추출 시작")
    enricher = ContentEnricher.create_default(
        cache_dir=SETTINGS.enrichment_cache_dir,
        timeout_seconds=SETTINGS.enrichment_timeout_seconds,
        max_attempts=SETTINGS.enrichment_max_attempts,
        minimum_tokens=SETTINGS.enrichment_minimum_tokens,
        full_content_max_tokens=SETTINGS.enrichment_full_content_max_tokens,
        chunk_selection_max_tokens=SETTINGS.enrichment_chunk_selection_max_tokens,
        chunk_max_tokens=SETTINGS.enrichment_chunk_max_tokens,
    )
    enrichment_result = enricher.enrich(preprocessing_result)
    enriched_paths = write_enrichment_result(
        SETTINGS.enriched_output_dir / generated_for,
        enrichment_result,
    )
    enriched_paths.extend(write_enrichment_trace(SETTINGS.trace_output_dir, enrichment_result))
    usable_count = sum(
        candidate.status.value in {"enriched", "fallback"}
        for candidate in enrichment_result.candidates
    )
    log_step(
        3,
        4,
        "Enrichment",
        (
            f"완료: candidates={len(enrichment_result.candidates)}, "
            f"usable={usable_count}, files={len(enriched_paths)}"
        ),
    )

    # 4. Writer 단계: Agent가 후보를 편집 결과로 바꾸고 Generator가 Markdown을 생성한다.
    #    TODAYINTECH_WRITER_AGENT=draft|openai 값으로 Draft 또는 OpenAI Agent를 선택한다.
    log_step(4, 4, "Writer", "Agent 브리핑 생성 및 Markdown 작성 시작")
    writer = NewsWriter(
        agent=create_news_editor_agent(SETTINGS),
        output_dir=SETTINGS.output_dir,
        briefed_article_store=briefed_article_store,
        trace_output_dir=SETTINGS.trace_output_dir,
        agent_name=SETTINGS.writer_agent,
    )
    writer_result = writer.write(enrichment_result)
    written_articles = sum(
        len(service.briefings) for service in writer_result.editorial_result.services
    )
    log_step(
        4,
        4,
        "Writer",
        f"완료: articles={written_articles}, files={len(writer_result.written_paths)}",
    )
    return writer_result


def main() -> None:
    result = run_pipeline()
    print(f"Generated writer output for {result.generated_for}")
    print(f"Written files: {len(result.written_paths)}")


if __name__ == "__main__":
    main()
