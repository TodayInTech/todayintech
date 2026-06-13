import json
from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text
from src.writer.agent.schemas import ServiceWritingResult


def write_service_index_markdown(output_root: Path, service: ServiceWritingResult) -> Path:
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
        "## 브리핑 글",
        "",
    ]

    if not service.briefings:
        lines.extend(["아직 Writer가 생성한 글이 없습니다.", ""])
    else:
        for briefing in service.briefings:
            relative_article_path = (
                f"../articles/{service.service_key}/{briefing.suggested_doc_key}.md"
            )
            title = mdx_safe_link_label(briefing.title)
            description = (
                briefing.briefing_body_ko
                or "News Editor Agent가 브리핑 본문을 작성하기 전의 draft 문서입니다."
            )
            lines.append(
                f"- [{title}]({relative_article_path})"
                f"  {mdx_safe_plain_text(description.splitlines()[0])} "
                f"`{briefing.editorial_status.value}` / score {briefing.candidate_score}"
            )
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
