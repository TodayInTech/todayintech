from datetime import UTC, datetime

from src.writer.agent.schemas import (
    ArticleBriefing,
    EditorialStatus,
    GenerationMethod,
)
from src.writer.generator.article_markdown_writer import write_article_markdown


def test_article_markdown_writer_renders_published_briefing_as_natural_article(
    tmp_path,
) -> None:
    briefing = ArticleBriefing(
        candidate_id="openai-blog:abc123",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        title="OpenAI Developer Update",
        source_url="https://openai.com/news/update",
        normalized_url="https://openai.com/news/update",
        title_fingerprint="openai developer update",
        published_at=datetime(2026, 6, 10, tzinfo=UTC),
        collected_at=datetime(2026, 6, 11, tzinfo=UTC),
        feed_summary="Feed summary",
        candidate_score=42,
        ranking_signals={"source_priority": 10},
        suggested_doc_key="2026-06-openai-developer-update-abc123",
        article_doc_path="docs/services/openai-blog/2026-06-openai-developer-update-abc123.md",
        editorial_status=EditorialStatus.PUBLISHED,
        generation_method=GenerationMethod.LLM,
        category="AI",
        importance_level="High",
        confidence_score=0.82,
        summary_scope="feed_metadata_only",
        publish_reason_ko="개발자 워크플로에 영향을 줄 수 있는 업데이트입니다.",
        evidence_basis_ko=["피드 설명이 개발자 도구 업데이트를 언급합니다."],
        summary_ko=(
            "OpenAI가 개발자용 도구를 개선한 배경과 주요 변경 사항을 설명합니다. "
            "이번 업데이트는 AI 기능을 제품에 연결하고 운영하는 과정을 효율화하는 데 초점을 맞춥니다.\n\n"
            "개발자는 반복적인 통합 작업을 줄이고 제품의 핵심 기능에 더 집중할 수 있습니다. "
            "세부 API 조건과 적용 범위는 원문에서 확인할 필요가 있습니다."
        ),
    )

    output_path = write_article_markdown(tmp_path, briefing)
    content = output_path.read_text(encoding="utf-8")

    assert "> OpenAI Blog · 2026-06-10 · AI" in content
    assert "OpenAI가 개발자용 도구를 개선한 배경" in content
    assert "OpenAI Blog에서 원문 읽기 →" in content
    assert "## 선정 이유" not in content
    assert "## 판단 근거 범위" not in content
    assert "## 사용한 근거" not in content
    assert "## 핵심 포인트" not in content
    assert "## 읽어볼 만한 이유" not in content
    assert "## 확인할 점" not in content
    assert "## 문서 정보" not in content
    assert "## 후보 판단 근거" not in content
