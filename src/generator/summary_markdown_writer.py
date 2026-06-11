from collections import defaultdict
from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text
from src.models import BriefingBundle


def write_summary_markdown(base_dir: Path, bundle: BriefingBundle) -> Path:
    base_dir.mkdir(parents=True, exist_ok=True)
    output_path = base_dir / "summary.md"
    by_category: dict[str, list[str]] = defaultdict(list)

    for service in bundle.service_briefings:
        for item in service.summaries:
            service_link = f"./services/{service.service_key}.md"
            source_link = str(item.article.url)
            title = mdx_safe_link_label(item.article.title)
            by_category[item.category.value].append(
                f"- {title} ([서비스 문서]({service_link}) / [원문]({source_link}))"
            )

    lines = [
        "# Today in Tech",
        "",
        f"생성일: {bundle.generated_for}",
        "",
        "## 개요",
        "",
        mdx_safe_plain_text(bundle.insight_ko) or "MVP 단계의 자동 생성 브리핑입니다.",
        "",
        "## 도메인별 시사점",
        "",
    ]

    if not by_category:
        lines.extend(["선별된 뉴스가 없습니다.", ""])

    for category, items in sorted(by_category.items()):
        lines.extend([f"### {category}", ""])
        lines.extend(items)
        lines.append("")

    lines.extend(["## 서비스별 브리핑", ""])
    for service in bundle.service_briefings:
        service_name = mdx_safe_link_label(service.service_name)
        lines.append(f"- [{service_name}](./services/{service.service_key}.md)")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
