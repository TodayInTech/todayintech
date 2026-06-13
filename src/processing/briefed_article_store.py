import json
from datetime import UTC, datetime
from pathlib import Path

from pydantic import BaseModel, Field

from src.processing.candidate_identity import url_hash


class BriefedArticleRecord(BaseModel):
    normalized_url: str
    title_fingerprint: str
    service_key: str
    title: str
    article_doc_path: str | None = None
    status: str = "published"
    briefed_at: datetime | None = None


class BriefedArticleState(BaseModel):
    version: int = 1
    articles: dict[str, BriefedArticleRecord] = Field(default_factory=dict)


class BriefedArticleStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.state = self._load()

    def contains(self, normalized_url: str, title_fingerprint: str, service_key: str) -> bool:
        url_key = self.key_for_url(normalized_url)
        if url_key in self.state.articles:
            return True

        return any(
            record.service_key == service_key
            and record.title_fingerprint == title_fingerprint
            and record.status in {"briefed", "published"}
            for record in self.state.articles.values()
        )

    def mark_published(
        self,
        *,
        normalized_url: str,
        title_fingerprint: str,
        service_key: str,
        title: str,
        article_doc_path: str | None = None,
    ) -> None:
        self.state.articles[self.key_for_url(normalized_url)] = BriefedArticleRecord(
            normalized_url=normalized_url,
            title_fingerprint=title_fingerprint,
            service_key=service_key,
            title=title,
            article_doc_path=article_doc_path,
            briefed_at=datetime.now(UTC),
        )

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self.state.model_dump(mode="json"), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def _load(self) -> BriefedArticleState:
        if not self.path.exists():
            return BriefedArticleState()

        return BriefedArticleState.model_validate_json(self.path.read_text(encoding="utf-8"))

    @staticmethod
    def key_for_url(normalized_url: str) -> str:
        return url_hash(normalized_url)
