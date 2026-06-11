from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text, mdx_safe_text
from src.models import ServiceBriefing


def write_service_markdown(base_dir: Path, briefing: ServiceBriefing) -> Path:
    services_dir = base_dir / "services"
    services_dir.mkdir(parents=True, exist_ok=True)
    output_path = services_dir / f"{briefing.service_key}.md"

    lines = [
        f"# {briefing.service_name}",
        "",
        f"생성일: {briefing.generated_for}",
        "",
        "## 주요 뉴스",
        "",
    ]

    if not briefing.summaries:
        lines.extend(["선별된 뉴스가 없습니다.", ""])

    for item in briefing.summaries:
        title = mdx_safe_plain_text(item.article.title)
        source = mdx_safe_link_label(item.article.source)
        summary = mdx_safe_text(item.summary_ko)
        why_it_matters = mdx_safe_plain_text(item.why_it_matters_ko)
        lines.extend(
            [
                f"### {title}",
                "",
                f"- 카테고리: {item.category.value}",
                f"- 중요도: {item.importance_score}/5",
                f"- 출처: [{source}]({item.article.url})",
                "",
                summary,
                "",
                "**왜 중요한가?**",
                "",
                why_it_matters,
                "",
                "---",
                "",
            ]
        )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
