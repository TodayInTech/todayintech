import json
from pathlib import Path

from src.generator.markdown_safety import mdx_safe_plain_text
from src.processing.models import ArchivedArticle
from src.writer.agent.schemas import ServiceWritingResult

EN_DOCS_PATH = Path("i18n/en/docusaurus-plugin-content-docs/current")

SERVICE_LABELS = {
    "ko": {
        "featured": "추천 글",
        "new": "새로운 글",
        "list": "브리핑 리스트",
    },
    "en": {
        "featured": "Recommended Articles",
        "new": "New Articles",
        "list": "Briefing List",
    },
}


def write_service_index_markdown(
    output_root: Path,
    service: ServiceWritingResult,
    archived_articles: list[ArchivedArticle],
    *,
    locale: str = "ko",
) -> Path:
    output_path = (
        _localized_output_root(output_root, locale) / "services" / f"{service.service_key}.md"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    service_name = mdx_safe_plain_text(service.service_name)
    labels = SERVICE_LABELS[locale]

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
        f"## {labels['featured']}",
        "",
        f'<BriefingList mode="featured" serviceKey="{service.service_key}" />',
        "",
        f"## {labels['new']}",
        "",
        f'<BriefingList mode="new" serviceKey="{service.service_key}" />',
        "",
        f"## {labels['list']}",
        "",
        f'<BriefingList serviceKey="{service.service_key}" />',
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
