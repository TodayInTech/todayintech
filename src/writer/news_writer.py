from pathlib import Path

from pydantic import BaseModel, Field

from src.processing.article_candidate import ArchivedArticle, PreprocessingResult
from src.processing.briefed_article_store import BriefedArticleStore
from src.progress import log_info
from src.writer.agent.contracts import NewsEditorAgent
from src.writer.agent.schemas import EditorialResult, EditorialStatus
from src.writer.generator.article_markdown_writer import write_article_markdown
from src.writer.generator.main_index_writer import write_main_index_markdown
from src.writer.generator.service_index_writer import write_service_index_markdown


class WriterResult(BaseModel):
    generated_for: str
    editorial_result: EditorialResult
    written_paths: list[Path] = Field(default_factory=list)


class NewsWriter:
    def __init__(
        self,
        *,
        agent: NewsEditorAgent,
        output_dir: Path,
        briefed_article_store: BriefedArticleStore,
    ) -> None:
        self.agent = agent
        self.output_dir = output_dir
        self.briefed_article_store = briefed_article_store

    def write(self, preprocessing_result: PreprocessingResult) -> WriterResult:
        log_info("Writer", "1. Agent 편집 결과 생성 시작")
        editorial_result = self.agent.edit(preprocessing_result)
        total_briefings = sum(len(service.briefings) for service in editorial_result.services)
        log_info(
            "Writer",
            f"1. Agent 편집 결과 생성 완료: services={len(editorial_result.services)}, briefings={total_briefings}",
        )
        written_paths: list[Path] = []

        log_info("Writer", "2. Markdown 파일 작성 시작")
        for service in editorial_result.services:
            log_info(
                "Writer",
                f"2. {service.service_key} article 작성: count={len(service.briefings)}",
            )
            for briefing in service.briefings:
                written_paths.append(write_article_markdown(self.output_dir, briefing))

        log_info("Writer", "3. briefed_articles 상태 갱신 시작")
        for service in editorial_result.services:
            for briefing in service.briefings:
                if briefing.editorial_status == EditorialStatus.PUBLISHED:
                    self.briefed_article_store.mark_published(
                        normalized_url=briefing.normalized_url,
                        title_fingerprint=briefing.title_fingerprint,
                        service_key=briefing.service_key,
                        title=briefing.title,
                        article_doc_path=briefing.article_doc_path,
                        candidate_score=briefing.candidate_score,
                    )
                else:
                    self.briefed_article_store.mark_draft(
                        normalized_url=briefing.normalized_url,
                        title_fingerprint=briefing.title_fingerprint,
                        service_key=briefing.service_key,
                        title=briefing.title,
                        article_doc_path=briefing.article_doc_path,
                        candidate_score=briefing.candidate_score,
                    )
        self.briefed_article_store.save()
        log_info("Writer", "3. briefed_articles 상태 갱신 완료")

        archived_articles = self._archive_articles_for_indexes(
            preprocessing_result, editorial_result
        )
        for service in editorial_result.services:
            written_paths.append(
                write_service_index_markdown(self.output_dir, service, archived_articles)
            )

        written_paths.append(
            write_main_index_markdown(self.output_dir, editorial_result, archived_articles)
        )
        log_info("Writer", f"2. Markdown 파일 작성 완료: files={len(written_paths)}")

        return WriterResult(
            generated_for=preprocessing_result.generated_for,
            editorial_result=editorial_result,
            written_paths=written_paths,
        )

    def _archive_articles_for_indexes(
        self,
        preprocessing_result: PreprocessingResult,
        editorial_result: EditorialResult,
    ) -> list[ArchivedArticle]:
        archived_by_path = {
            article.article_doc_path: article for article in preprocessing_result.archived_articles
        }
        for service in editorial_result.services:
            for briefing in service.briefings:
                archived_by_path[briefing.article_doc_path] = ArchivedArticle(
                    service_key=briefing.service_key,
                    service_name=briefing.service_name,
                    title=briefing.title,
                    article_doc_path=briefing.article_doc_path,
                    status=briefing.editorial_status.value,
                    briefed_at=None,
                    candidate_score=briefing.candidate_score,
                )
        return sorted(
            archived_by_path.values(),
            key=lambda item: (
                item.candidate_score,
                item.briefed_at.isoformat() if item.briefed_at else "",
            ),
            reverse=True,
        )
