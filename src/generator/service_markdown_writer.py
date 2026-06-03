from pathlib import Path

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
        lines.extend(
            [
                f"### {item.article.title}",
                "",
                f"- 카테고리: {item.category.value}",
                f"- 중요도: {item.importance_score}/5",
                f"- 출처: [{item.article.source}]({item.article.url})",
                "",
                item.summary_ko,
                "",
                "**왜 중요한가?**",
                "",
                item.why_it_matters_ko,
                "",
                "---",
                "",
            ]
        )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
