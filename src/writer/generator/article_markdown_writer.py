import json
from pathlib import Path

from src.generator.markdown_safety import mdx_safe_link_label, mdx_safe_plain_text, mdx_safe_text
from src.writer.agent.schemas import ArticleBriefing, EditorialStatus


def write_article_markdown(output_root: Path, briefing: ArticleBriefing) -> Path:
    output_path = (
        output_root / "services" / briefing.service_key / f"{briefing.suggested_doc_key}.md"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    published_date = (
        briefing.published_at.date().isoformat() if briefing.published_at else "날짜 미상"
    )
    category = briefing.category or briefing.editorial_status.value
    lines = [
        "---",
        f"title: {json.dumps(mdx_safe_plain_text(briefing.title), ensure_ascii=False)}",
        f"sidebar_label: {json.dumps(mdx_safe_plain_text(briefing.title), ensure_ascii=False)}",
        "---",
        "",
        f"# {mdx_safe_plain_text(briefing.title)}",
        "",
        f"> {mdx_safe_plain_text(briefing.service_name)} · {published_date} · {mdx_safe_plain_text(category)}",
        "",
        f"원문 링크: [{mdx_safe_link_label(briefing.title)}]({briefing.source_url})",
        "",
        "---",
        "",
    ]

    if briefing.editorial_status == EditorialStatus.PUBLISHED:
        lines.extend(_published_lines(briefing))
    else:
        lines.extend(_draft_lines(briefing))

    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def _published_lines(briefing: ArticleBriefing) -> list[str]:
    lines: list[str] = []

    body = mdx_safe_text(briefing.briefing_body_ko or "")
    lines.extend([body or "브리핑 본문이 아직 생성되지 않았습니다.", ""])

    decision_lines = _decision_context_lines(briefing)
    if decision_lines:
        lines.extend(decision_lines)

    if briefing.key_points_ko:
        lines.extend(["## 핵심 포인트", ""])
        for point in briefing.key_points_ko:
            lines.append(f"- {mdx_safe_plain_text(point)}")
        lines.append("")

    if briefing.why_it_matters_ko:
        lines.extend(
            [
                "## 읽어볼 만한 이유",
                "",
                mdx_safe_text(briefing.why_it_matters_ko),
                "",
            ]
        )

    if briefing.caveats_ko:
        lines.extend(["## 확인할 점", ""])
        for caveat in briefing.caveats_ko:
            lines.append(f"- {mdx_safe_plain_text(caveat)}")
        lines.append("")

    lines.extend(_metadata_lines(briefing))
    return lines


def _decision_context_lines(briefing: ArticleBriefing) -> list[str]:
    lines: list[str] = []
    if briefing.publish_reason_ko:
        lines.extend(["## 선정 이유", "", mdx_safe_text(briefing.publish_reason_ko), ""])

    if briefing.summary_scope or briefing.confidence_score is not None:
        lines.extend(["## 판단 근거 범위", ""])
        if briefing.summary_scope:
            lines.append(f"- 요약 범위: `{mdx_safe_plain_text(briefing.summary_scope)}`")
        if briefing.confidence_score is not None:
            lines.append(f"- 판단 확신도: {briefing.confidence_score:.2f}")
        lines.append("")

    if briefing.evidence_basis_ko:
        lines.extend(["## 사용한 근거", ""])
        for evidence in briefing.evidence_basis_ko:
            lines.append(f"- {mdx_safe_plain_text(evidence)}")
        lines.append("")

    return lines


def _draft_lines(briefing: ArticleBriefing) -> list[str]:
    lines = [
        "아직 News Editor Agent가 브리핑 본문을 작성하지 않았습니다.",
        "",
        "## 피드에서 제공된 설명",
        "",
    ]
    feed_summary = mdx_safe_text(briefing.feed_summary)
    lines.extend([feed_summary or "피드에서 제공한 설명이 없습니다.", ""])

    lines.extend(
        [
            "## 후보 판단 근거",
            "",
            f"- 후보 ID: `{briefing.candidate_id}`",
            f"- 후보 점수: {briefing.candidate_score}",
            f"- 편집 상태: `{briefing.editorial_status.value}`",
            f"- 생성 방식: `{briefing.generation_method.value}`",
        ]
    )

    ranking_signals = briefing.ranking_signals.compact_dict()
    if ranking_signals:
        for key, value in sorted(ranking_signals.items()):
            lines.append(f"- `{key}`: {mdx_safe_plain_text(str(value))}")
    else:
        lines.append("- 기록된 ranking signal이 없습니다.")

    if briefing.ranking_reasons_ko:
        lines.append("")
        lines.append("### 점수 산정 설명")
        lines.append("")
        for reason in briefing.ranking_reasons_ko:
            lines.append(f"- {mdx_safe_plain_text(reason)}")

    lines.extend(["", *_metadata_lines(briefing)])
    return lines


def _metadata_lines(briefing: ArticleBriefing) -> list[str]:
    return [
        "## 문서 정보",
        "",
        f"- 수집일: {briefing.collected_at.isoformat()}",
        f"- 후보 ID: `{briefing.candidate_id}`",
        f"- 후보 점수: {briefing.candidate_score}",
        f"- 편집 상태: `{briefing.editorial_status.value}`",
        f"- 생성 방식: `{briefing.generation_method.value}`",
        "",
    ]
