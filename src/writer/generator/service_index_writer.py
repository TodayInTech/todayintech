import json
from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text
from src.processing.article_candidate import ArchivedArticle
from src.writer.agent.schemas import ServiceWritingResult

SERVICE_PRIORITY_LIMIT = 4


def write_service_index_markdown(
    output_root: Path,
    service: ServiceWritingResult,
    archived_articles: list[ArchivedArticle],
) -> Path:
    output_path = output_root / "services" / f"{service.service_key}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "---",
        f"title: {json.dumps(mdx_safe_plain_text(service.service_name), ensure_ascii=False)}",
        f"sidebar_label: {json.dumps(mdx_safe_plain_text(service.service_name), ensure_ascii=False)}",
        "---",
        "",
        f"# {mdx_safe_plain_text(service.service_name)}",
        "",
        f"{mdx_safe_plain_text(service.service_name)}에서 선별된 글 브리핑을 모아둔 서비스 페이지입니다.",
        "",
        "## 우선순위 브리핑",
        "",
    ]

    service_records = [
        record
        for record in sorted(
            archived_articles,
            key=lambda item: (
                item.candidate_score,
                item.briefed_at.isoformat() if item.briefed_at else "",
            ),
            reverse=True,
        )
        if record.service_key == service.service_key and record.article_doc_path
    ]
    priority_records = service_records[:SERVICE_PRIORITY_LIMIT]

    if not priority_records:
        lines.extend(["아직 우선순위로 표시할 브리핑 글이 없습니다.", ""])
    else:
        for record in priority_records:
            relative_article_path = _relative_service_article_path(
                service.service_key,
                record.article_doc_path or "",
            )
            title = mdx_safe_link_label(record.title)
            lines.append(
                f"- [{title}]({relative_article_path})"
                f" `{mdx_safe_plain_text(record.status)}` / score {record.candidate_score}"
            )
        lines.append("")

    lines.extend(["## 누적 브리핑 목록", ""])
    if not service_records:
        lines.extend(["아직 누적된 브리핑 글이 없습니다.", ""])
    else:
        for record in service_records:
            relative_article_path = _relative_service_article_path(
                service.service_key,
                record.article_doc_path or "",
            )
            title = mdx_safe_link_label(record.title)
            lines.append(
                f"- [{title}]({relative_article_path}) `{mdx_safe_plain_text(record.status)}`"
            )
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def _relative_service_article_path(service_key: str, article_doc_path: str) -> str:
    prefix = f"docs/services/{service_key}/"
    if article_doc_path.startswith(prefix):
        return f"./{service_key}/{article_doc_path.removeprefix(prefix)}"
    return article_doc_path
