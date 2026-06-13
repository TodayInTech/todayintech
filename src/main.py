from src.collection import NewsCollector, write_raw_collection_results
from src.processing import BriefedArticleStore, NewsPreprocessor
from src.processing.processed_writer import write_preprocessing_result
from src.settings import SETTINGS
from src.sources import NewsSourceFactory
from src.writer import DraftNewsEditorAgent, NewsWriter, WriterResult


def run_pipeline(target_date: str | None = None) -> WriterResult:
    generated_for = SETTINGS.resolve_target_date(target_date)

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

    # 3. Writer 단계: Agent가 후보를 편집 결과로 바꾸고 Generator가 Markdown을 생성한다.
    #    현재 Agent는 요약을 만들지 않는 Draft Agent이며, LLM Agent는 이후 같은 계약으로 교체한다.
    writer = NewsWriter(
        agent=DraftNewsEditorAgent(),
        output_dir=SETTINGS.output_dir,
        briefed_article_store=briefed_article_store,
    )
    return writer.write(preprocessing_result)


def main() -> None:
    result = run_pipeline()
    print(f"Generated writer output for {result.generated_for}")
    print(f"Written files: {len(result.written_paths)}")


if __name__ == "__main__":
    main()
