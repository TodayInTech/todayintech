import json
from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text, mdx_safe_text
from src.writer.agent.schemas import ArticleBriefing


def write_article_markdown(output_root: Path, briefing: ArticleBriefing) -> Path:
    output_path = (
        output_root / "articles" / briefing.service_key / f"{briefing.suggested_doc_key}.md"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "---",
        f"title: {json.dumps(mdx_safe_plain_text(briefing.title), ensure_ascii=False)}",
        f"sidebar_label: {json.dumps(mdx_safe_plain_text(briefing.title), ensure_ascii=False)}",
        "---",
        "",
        f"# {mdx_safe_plain_text(briefing.title)}",
        "",
        "## 메타데이터",
        "",
        f"- 서비스: {mdx_safe_plain_text(briefing.service_name)}",
        f"- 원문: [{mdx_safe_link_label(briefing.title)}]({briefing.source_url})",
        f"- 발행일: {briefing.published_at.isoformat() if briefing.published_at else '알 수 없음'}",
        f"- 수집일: {briefing.collected_at.isoformat()}",
        f"- 후보 ID: `{briefing.candidate_id}`",
        f"- 후보 점수: {briefing.candidate_score}",
        f"- 편집 상태: `{briefing.editorial_status.value}`",
        f"- 생성 방식: `{briefing.generation_method.value}`",
        "",
        "## 피드 설명",
        "",
    ]

    feed_summary = mdx_safe_text(briefing.feed_summary)
    lines.extend([feed_summary or "피드에서 제공한 설명이 없습니다.", ""])

    lines.extend(
        [
            "## 편집 상태",
            "",
            "이 문서는 Draft Writer가 생성한 초안입니다. 요약, 중요성 판단, 개발자 관점 인사이트는 News Editor Agent가 생성한 뒤 게시 상태로 전환합니다.",
            "",
            "## 판단 근거",
            "",
        ]
    )

    if briefing.ranking_signals:
        for key, value in sorted(briefing.ranking_signals.items()):
            lines.append(f"- `{key}`: {mdx_safe_plain_text(str(value))}")
    else:
        lines.append("- 기록된 ranking signal이 없습니다.")

    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
