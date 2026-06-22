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
        briefing_body_ko=(
            "OpenAI의 개발자 업데이트를 다룬 글입니다.\n\n"
            "개발 환경에서 AI 도구를 어떻게 접목할지 살펴볼 만합니다."
        ),
        key_points_ko=["개발자 도구 업데이트", "AI 도입 흐름"],
        why_it_matters_ko="개발 워크플로 변화와 직접 연결될 수 있기 때문입니다.",
        caveats_ko=["세부 API 조건은 원문 확인이 필요합니다."],
    )

    output_path = write_article_markdown(tmp_path, briefing)
    content = output_path.read_text(encoding="utf-8")

    assert "> OpenAI Blog · 2026-06-10 · AI" in content
    assert "OpenAI의 개발자 업데이트를 다룬 글입니다." in content
    assert "## 선정 이유" in content
    assert "개발자 워크플로에 영향을 줄 수 있는 업데이트입니다." in content
    assert "## 판단 근거 범위" in content
    assert "- 요약 범위: `feed_metadata_only`" in content
    assert "- 판단 확신도: 0.82" in content
    assert "## 사용한 근거" in content
    assert "## 핵심 포인트" in content
    assert "- 개발자 도구 업데이트" in content
    assert "## 읽어볼 만한 이유" in content
    assert "## 확인할 점" in content
    assert "## 후보 판단 근거" not in content
