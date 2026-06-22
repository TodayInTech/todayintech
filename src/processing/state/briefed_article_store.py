import json
from datetime import UTC, datetime
from pathlib import Path

from pydantic import BaseModel, Field

from src.processing.identity.candidate_identity import url_hash

ACTIVE_BRIEFING_STATUSES = {"draft", "briefed", "published"}


class BriefedArticleRecord(BaseModel):
    normalized_url: str
    title_fingerprint: str
    service_key: str
    title: str
    article_doc_path: str | None = None
    status: str = "published"
    briefed_at: datetime | None = None
    candidate_score: float = 0


class BriefedArticleState(BaseModel):
    version: int = 1
    articles: dict[str, BriefedArticleRecord] = Field(default_factory=dict)


class BriefedArticleStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.state = self._load()

    def contains(
        self,
        normalized_url: str,
        title_fingerprint: str,
        service_key: str,
        article_doc_path: str | None = None,
    ) -> bool:
        url_key = self.key_for_url(normalized_url)
        if (
            url_key in self.state.articles
            and self.state.articles[url_key].status in ACTIVE_BRIEFING_STATUSES
        ):
            return True

        if any(
            record.service_key == service_key
            and record.title_fingerprint == title_fingerprint
            and record.status in ACTIVE_BRIEFING_STATUSES
            for record in self.state.articles.values()
        ):
            return True

        return bool(article_doc_path and Path(article_doc_path).exists())

    def active_records(self) -> list[BriefedArticleRecord]:
        return [
            record
            for record in self.state.articles.values()
            if record.status in ACTIVE_BRIEFING_STATUSES
        ]

    def mark_published(
        self,
        *,
        normalized_url: str,
        title_fingerprint: str,
        service_key: str,
        title: str,
        article_doc_path: str | None = None,
        candidate_score: float = 0,
    ) -> None:
        self.mark(
            normalized_url=normalized_url,
            title_fingerprint=title_fingerprint,
            service_key=service_key,
            title=title,
            article_doc_path=article_doc_path,
            candidate_score=candidate_score,
            status="published",
        )

    def mark_draft(
        self,
        *,
        normalized_url: str,
        title_fingerprint: str,
        service_key: str,
        title: str,
        article_doc_path: str | None = None,
        candidate_score: float = 0,
    ) -> None:
        self.mark(
            normalized_url=normalized_url,
            title_fingerprint=title_fingerprint,
            service_key=service_key,
            title=title,
            article_doc_path=article_doc_path,
            candidate_score=candidate_score,
            status="draft",
        )

    def mark(
        self,
        *,
        normalized_url: str,
        title_fingerprint: str,
        service_key: str,
        title: str,
        article_doc_path: str | None = None,
        candidate_score: float = 0,
        status: str,
    ) -> None:
        self.state.articles[self.key_for_url(normalized_url)] = BriefedArticleRecord(
            normalized_url=normalized_url,
            title_fingerprint=title_fingerprint,
            service_key=service_key,
            title=title,
            article_doc_path=article_doc_path,
            status=status,
            briefed_at=datetime.now(UTC),
            candidate_score=candidate_score,
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
