from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text
from src.writer.agent.schemas import EditorialResult


def write_main_index_markdown(output_root: Path, editorial_result: EditorialResult) -> Path:
    output_path = output_root / "index.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "---",
        "title: Today in Tech",
        "sidebar_label: Overview",
        "---",
        "",
        "# Today in Tech",
        "",
        f"생성일: {editorial_result.generated_for}",
        "",
        "## 개요",
        "",
        "Today in Tech는 수집된 기술 글 후보를 Writer 단계에서 문서화하는 큐레이션 아카이브입니다.",
        "",
        "## 최근 Writer 초안",
        "",
    ]

    written_any = False
    for service in editorial_result.services:
        for briefing in service.briefings:
            written_any = True
            article_path = f"./articles/{service.service_key}/{briefing.suggested_doc_key}.md"
            title = mdx_safe_link_label(briefing.title)
            service_name = mdx_safe_plain_text(service.service_name)
            lines.append(
                f"- [{title}]({article_path}) "
                f"- {service_name} / `{briefing.editorial_status.value}`"
            )

    if not written_any:
        lines.append("아직 Writer가 생성한 글이 없습니다.")

    lines.extend(["", "## 서비스", ""])
    for service in editorial_result.services:
        service_name = mdx_safe_link_label(service.service_name)
        lines.append(f"- [{service_name}](./services/{service.service_key}.md)")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
