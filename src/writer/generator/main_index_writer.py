from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text
from src.processing.article_candidate import ArchivedArticle
from src.writer.agent.schemas import EditorialResult

MAIN_PRIORITY_LIMIT = 20


def write_main_index_markdown(
    output_root: Path,
    editorial_result: EditorialResult,
    archived_articles: list[ArchivedArticle],
) -> Path:
    output_path = output_root / "index.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "---",
        "title: Today in Tech",
        "sidebar_label: Today in Tech",
        "---",
        "",
        "# Today in Tech",
        "",
        f"생성일: {editorial_result.generated_for}",
        "",
        "## 개요",
        "",
        "Today in Tech는 여러 기술 서비스에서 수집한 글을 선별해 읽기 쉬운 브리핑으로 정리하는 큐레이션 아카이브입니다.",
        "",
        "## 우선순위 브리핑",
        "",
    ]

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
    service_names = {
        service.service_key: service.service_name for service in editorial_result.services
    }

    if not priority_records:
        lines.append("아직 우선순위로 표시할 브리핑 글이 없습니다.")
    else:
        for record in priority_records:
            article_path = _relative_article_path(record.article_doc_path or "")
            title = mdx_safe_link_label(record.title)
            service_name = mdx_safe_plain_text(
                service_names.get(record.service_key, record.service_key)
            )
            lines.append(
                f"- [{title}]({article_path}) "
                f"- {service_name} `{mdx_safe_plain_text(record.status)}` "
                f"/ score {record.candidate_score}"
            )

    new_briefings = sorted(
        (
            (service.service_name, briefing)
            for service in editorial_result.services
            for briefing in service.briefings
        ),
        key=lambda item: item[1].candidate_score,
        reverse=True,
    )

    lines.extend(["", "## 이번 실행에서 추가된 글", ""])
    if not new_briefings:
        lines.append("이번 실행에서 새로 생성된 글은 없습니다.")
    else:
        for service_name, briefing in new_briefings:
            article_path = f"./services/{briefing.service_key}/{briefing.suggested_doc_key}.md"
            title = mdx_safe_link_label(briefing.title)
            description = briefing.briefing_body_ko or "브리핑 본문 작성 대기"
            lines.append(
                f"- [{title}]({article_path}) "
                f"- {mdx_safe_plain_text(service_name)} / {mdx_safe_plain_text(description.splitlines()[0])} "
                f"`{briefing.editorial_status.value}` / score {briefing.candidate_score}"
            )

    lines.extend(["", "## 서비스", ""])
    for service in editorial_result.services:
        service_name = mdx_safe_link_label(service.service_name)
        lines.append(f"- [{service_name}](./services/{service.service_key}.md)")
    lines.append("")

    lines.extend(["## 누적 브리핑 목록", ""])
    if not active_records:
        lines.append("아직 누적된 브리핑 글이 없습니다.")
    else:
        for record in active_records:
            title = mdx_safe_link_label(record.title)
            service_name = mdx_safe_plain_text(
                service_names.get(record.service_key, record.service_key)
            )
            article_path = _relative_article_path(record.article_doc_path or "")
            lines.append(
                f"- [{title}]({article_path}) "
                f"- {service_name} `{mdx_safe_plain_text(record.status)}`"
            )
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def _relative_article_path(article_doc_path: str) -> str:
    prefix = "docs/"
    if article_doc_path.startswith(prefix):
        return f"./{article_doc_path.removeprefix(prefix)}"
    return article_doc_path
