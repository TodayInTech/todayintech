from pathlib import Path

from pydantic import BaseModel, Field

from src.processing.article_candidate import PreprocessingResult
from src.processing.briefed_article_store import BriefedArticleStore
from src.writer.agent.contracts import NewsEditorAgent
from src.writer.agent.schemas import EditorialResult
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
        editorial_result = self.agent.edit(preprocessing_result)
        written_paths: list[Path] = []

        for service in editorial_result.services:
            for briefing in service.briefings:
                written_paths.append(write_article_markdown(self.output_dir, briefing))
            written_paths.append(write_service_index_markdown(self.output_dir, service))

        written_paths.append(write_main_index_markdown(self.output_dir, editorial_result))

        for service in editorial_result.services:
            for briefing in service.briefings:
                self.briefed_article_store.mark_draft(
                    normalized_url=briefing.normalized_url,
                    title_fingerprint=briefing.title_fingerprint,
                    service_key=briefing.service_key,
                    title=briefing.title,
                    article_doc_path=briefing.article_doc_path,
                )
        self.briefed_article_store.save()

        return WriterResult(
            generated_for=preprocessing_result.generated_for,
            editorial_result=editorial_result,
            written_paths=written_paths,
        )
