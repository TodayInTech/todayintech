import json
import re
from pathlib import Path

from src.processing.models import ArchivedArticle
from src.writer.agent.schemas import ArticleBriefing, EditorialResult

MAIN_PRIORITY_LIMIT = 20
MAIN_NEW_LIMIT = 20
BRIEFING_DATA_PATH = Path("static/data/briefings/index.json")
EN_DOCS_PATH = Path("i18n/en/docusaurus-plugin-content-docs/current")

MAIN_LABELS = {
    "ko": {
        "generated_for": "생성일",
        "featured": "추천 글",
        "new": "새로운 글",
        "list": "브리핑 리스트",
    },
    "en": {
        "generated_for": "Generated for",
        "featured": "Recommended Articles",
        "new": "New Articles",
        "list": "Briefing List",
    },
}


def write_main_index_markdown(
    output_root: Path,
    editorial_result: EditorialResult,
    archived_articles: list[ArchivedArticle],
    *,
    locale: str = "ko",
) -> Path:
    output_path = _localized_output_root(output_root, locale) / "index.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    labels = MAIN_LABELS[locale]

    service_names = {
        service.service_key: service.service_name for service in editorial_result.services
    }
    service_names.update(
        {
            record.service_key: record.service_name
            for record in archived_articles
            if record.service_name
        }
    )
    active_records = [
        record
        for record in sorted(
            archived_articles,
            key=lambda item: (
                item.candidate_score,
                item.briefed_at.isoformat() if item.briefed_at else "",
            ),
            reverse=True,
        )
        if record.article_doc_path
    ]
    priority_records = active_records[:MAIN_PRIORITY_LIMIT]
    new_briefings = sorted(
        (briefing for service in editorial_result.services for briefing in service.briefings),
        key=lambda briefing: briefing.candidate_score,
        reverse=True,
    )[:MAIN_NEW_LIMIT]

    if locale == "ko":
        _write_briefing_data(
            output_root=output_root,
            generated_for=editorial_result.generated_for,
            service_names=service_names,
            active_records=active_records,
            priority_records=priority_records,
            new_briefings=new_briefings,
        )

    lines = [
        "---",
        "title: Today in Tech",
        "sidebar_label: Today in Tech",
        "---",
        "",
        "# Today in Tech",
        "",
        f"{labels['generated_for']}: {editorial_result.generated_for}",
        "",
        f"## {labels['featured']}",
        "",
        '<BriefingList mode="featured" />',
        "",
        f"## {labels['new']}",
        "",
        '<BriefingList mode="new" />',
        "",
        f"## {labels['list']}",
        "",
        "<BriefingList />",
        "",
    ]

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def _localized_output_root(output_root: Path, locale: str) -> Path:
    if locale == "ko":
        return output_root
    if locale == "en":
        return output_root.parent / EN_DOCS_PATH
    msg = f"Unsupported docs locale: {locale}"
    raise ValueError(msg)


def _write_briefing_data(
    *,
    output_root: Path,
    generated_for: str,
    service_names: dict[str, str],
    active_records: list[ArchivedArticle],
    priority_records: list[ArchivedArticle],
    new_briefings: list[ArticleBriefing],
) -> None:
    data_path = output_root.parent / BRIEFING_DATA_PATH
    data_path.parent.mkdir(parents=True, exist_ok=True)
    priority_paths = {record.article_doc_path for record in priority_records}
    new_paths = {briefing.article_doc_path for briefing in new_briefings}
    if not new_paths:
        latest_briefed_at = max(
            (record.briefed_at for record in active_records if record.briefed_at),
            default=None,
        )
        if latest_briefed_at:
            latest_date = latest_briefed_at.date()
            new_paths = {
                record.article_doc_path
                for record in active_records
                if record.briefed_at and record.briefed_at.date() == latest_date
            }
    items = [
        _record_to_briefing_item(
            output_root=output_root,
            record=record,
            service_name=service_names.get(record.service_key, record.service_key),
            featured=record.article_doc_path in priority_paths,
            new=record.article_doc_path in new_paths,
        )
        for record in active_records
    ]
    data_path.write_text(
        json.dumps(
            {
                "generated_for": generated_for,
                "services": service_names,
                "items": items,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def _record_to_briefing_item(
    *,
    output_root: Path,
    record: ArchivedArticle,
    service_name: str,
    featured: bool,
    new: bool,
) -> dict[str, str | float | bool | None]:
    article_doc_path = record.article_doc_path or ""
    article_path = _relative_article_path(article_doc_path)
    article_file = output_root.parent / article_doc_path
    published_at, excerpt = _extract_article_card_content(article_file)
    return {
        "title": record.title,
        "service_key": record.service_key,
        "service_name": service_name,
        "href": article_path,
        "status": record.status,
        "score": record.candidate_score,
        "briefed_at": record.briefed_at.date().isoformat() if record.briefed_at else None,
        "published_at": published_at,
        "excerpt": excerpt,
        "featured": featured,
        "new": new,
    }


def _extract_article_card_content(article_path: Path) -> tuple[str | None, str]:
    if not article_path.exists():
        return None, ""

    text = article_path.read_text(encoding="utf-8")
    published_at = None
    for line in text.splitlines():
        if line.startswith("> "):
            parts = [part.strip() for part in line.removeprefix("> ").split("·")]
            if len(parts) >= 2:
                published_at = parts[1]
            break

    body = text.split("---", maxsplit=2)[-1]
    paragraphs = [
        _clean_markdown(paragraph)
        for paragraph in re.split(r"\n{2,}", body)
        if _is_summary_paragraph(paragraph)
    ]
    excerpt = " ".join(paragraphs[:2])
    return published_at, _truncate(excerpt, 180)


def _is_summary_paragraph(paragraph: str) -> bool:
    stripped = paragraph.strip()
    return bool(
        stripped
        and not stripped.startswith(("#", ">", "-", "[", "|", "<"))
        and "원문 링크:" not in stripped
    )


def _clean_markdown(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return re.sub(r"\s+", " ", value).strip()


def _truncate(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return f"{value[: limit - 1].rstrip()}…"


def _relative_article_path(article_doc_path: str) -> str:
    prefix = "docs/"
    if article_doc_path.startswith(prefix):
        return f"./{article_doc_path.removeprefix(prefix)}"
    return article_doc_path
