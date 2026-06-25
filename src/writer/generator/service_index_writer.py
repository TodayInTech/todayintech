import json
from pathlib import Path

from src.generator.markdown_safety import mdx_safe_plain_text
from src.processing.models import ArchivedArticle
from src.writer.agent.schemas import ServiceWritingResult


def write_service_index_markdown(
    output_root: Path,
    service: ServiceWritingResult,
    archived_articles: list[ArchivedArticle],
) -> Path:
    output_path = output_root / "services" / f"{service.service_key}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    service_name = mdx_safe_plain_text(service.service_name)

    lines = [
        "---",
        f"title: {json.dumps(service_name, ensure_ascii=False)}",
        f"sidebar_label: {json.dumps(service_name, ensure_ascii=False)}",
        "hide_title: true",
        "---",
        "",
        (
            f'<ServiceHeader serviceKey="{service.service_key}" '
            f"title={json.dumps(service_name, ensure_ascii=False)} />"
        ),
        "",
        "## 추천 글",
        "",
        f'<BriefingList mode="featured" serviceKey="{service.service_key}" />',
        "",
        "## 새로운 글",
        "",
        f'<BriefingList mode="new" serviceKey="{service.service_key}" />',
        "",
        "## 브리핑 리스트",
        "",
        f'<BriefingList serviceKey="{service.service_key}" />',
        "",
    ]

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
