from datetime import UTC, datetime
from types import SimpleNamespace

import pytest

from src.enrichment.models import (
    EnrichedArticleCandidate,
    EnrichmentInputStrategy,
    EnrichmentResult,
    EnrichmentStatus,
    EvidenceChunk,
    ExtractedDocument,
)
from src.models import Article
from src.processing.models import (
    ArticleCandidate,
    PreprocessingResult,
    ServicePreprocessingResult,
)
from src.writer.agent.openai_agent import OpenAINewsEditorAgent
from src.writer.agent.schemas import (
    AgentDecisionStatus,
    EditorialStatus,
    GenerationMethod,
    OpenAIArticleDecision,
)


class FakeResponses:
    def __init__(self, decision: OpenAIArticleDecision) -> None:
        self.decision = decision
        self.last_input = ""

    def parse(self, **kwargs):
        self.last_input = kwargs["input"]
        assert kwargs["text_format"] is OpenAIArticleDecision
        return SimpleNamespace(output_parsed=self.decision)


class FakeOpenAIClient:
    def __init__(self, decision: OpenAIArticleDecision) -> None:
        self.responses = FakeResponses(decision)


class RetryResponses:
    def __init__(self, decision: OpenAIArticleDecision) -> None:
        self.calls = 0
        self.decision = decision

    def parse(self, **kwargs):
        self.calls += 1
        assert kwargs["text_format"] is OpenAIArticleDecision
        if self.calls == 1:
            raise ValueError("Invalid JSON: EOF while parsing a string")
        return SimpleNamespace(output_parsed=self.decision)


class RetryOpenAIClient:
    def __init__(self, decision: OpenAIArticleDecision) -> None:
        self.responses = RetryResponses(decision)


def make_candidate() -> ArticleCandidate:
    article = Article(
        source="OpenAI Blog",
        title="OpenAI Developer Update",
        url="https://openai.com/news/update",
        published_at=datetime(2026, 6, 10, tzinfo=UTC),
        collected_at=datetime(2026, 6, 11, tzinfo=UTC),
        summary="Feed summary",
        metadata={"topic": "developer"},
    )
    return ArticleCandidate(
        candidate_id="openai-blog:abc123",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        article=article,
        normalized_url="https://openai.com/news/update",
        url_hash="abc123",
        title_fingerprint="openai developer update",
        feed_summary="<p>OpenAI developer feed summary</p>",
        suggested_doc_key="2026-06-openai-developer-update-abc123",
        suggested_article_path="docs/services/openai-blog/2026-06-openai-developer-update-abc123.md",
        candidate_score=42,
        ranking_signals={"source_priority": 10},
    )


def make_preprocessing_result() -> PreprocessingResult:
    return PreprocessingResult(
        generated_for="2026-06-11",
        generated_at=datetime(2026, 6, 11, tzinfo=UTC),
        raw_count=1,
        candidate_count=1,
        excluded_count=0,
        services=[
            ServicePreprocessingResult(
                service_key="openai-blog",
                service_name="OpenAI Blog",
                raw_count=1,
                candidate_count=1,
                excluded_count=0,
                candidates=[make_candidate()],
            )
        ],
    )


def make_enrichment_result(
    *,
    strategy: EnrichmentInputStrategy = EnrichmentInputStrategy.FULL_CONTENT,
    select_chunks: bool | None = None,
) -> EnrichmentResult:
    preprocessing = make_preprocessing_result()
    candidate = preprocessing.services[0].candidates[0]
    chunk = EvidenceChunk(
        chunk_id="chunk-0001",
        heading_path=["Developer update"],
        text="OpenAI describes concrete developer tooling changes and their integration context.",
        block_ids=["block-0001"],
        token_count=14,
        position=0,
    )
    should_select_chunks = (
        strategy == EnrichmentInputStrategy.FULL_CONTENT if select_chunks is None else select_chunks
    )
    selected_chunks = [chunk] if should_select_chunks else []
    return EnrichmentResult(
        generated_for=preprocessing.generated_for,
        generated_at=preprocessing.generated_at,
        candidates=[
            EnrichedArticleCandidate(
                candidate=candidate,
                status=EnrichmentStatus.ENRICHED,
                input_strategy=strategy,
                document=ExtractedDocument(
                    plain_text=chunk.text,
                    content_hash="abc",
                    char_count=len(chunk.text),
                    token_count=chunk.token_count,
                ),
                chunks=[chunk],
                selected_chunks=selected_chunks,
            )
        ],
    )


def test_openai_agent_creates_published_briefing_from_structured_output() -> None:
    decision = OpenAIArticleDecision(
        should_publish=True,
        category="AI",
        importance_level="High",
        confidence_score=0.82,
        summary_scope="full_content",
        publish_reason_ko="개발자 워크플로에 영향을 줄 수 있는 업데이트입니다.",
        evidence_basis_ko=["피드 설명이 개발자 업데이트를 언급합니다."],
        summary_ko=(
            "OpenAI가 개발자 도구를 업데이트한 배경과 주요 변화에 대해 설명합니다. "
            "피드 정보 기준으로는 AI 기능을 제품에 통합하는 과정을 개선하는 데 초점을 맞춥니다.\n\n"
            "개발자는 반복적인 설정과 연결 작업을 줄이고 핵심 기능 구현에 더 집중할 수 있습니다. "
            "구체적인 지원 범위와 적용 방법은 원문에서 추가로 확인할 필요가 있습니다."
        ),
    )
    client = FakeOpenAIClient(decision)
    agent = OpenAINewsEditorAgent(api_key=None, model="gpt-5-mini", client=client)

    result = agent.edit(make_enrichment_result())
    briefing = result.services[0].briefings[0]

    assert briefing.editorial_status == EditorialStatus.PUBLISHED
    assert briefing.generation_method == GenerationMethod.LLM
    assert briefing.category == "AI"
    assert briefing.importance_level == "High"
    assert briefing.confidence_score == 0.82
    assert briefing.summary_scope == "full_content"
    assert briefing.publish_reason_ko == "개발자 워크플로에 영향을 줄 수 있는 업데이트입니다."
    assert briefing.evidence_basis_ko == ["피드 설명이 개발자 업데이트를 언급합니다."]
    assert briefing.summary_ko == decision.summary_ko
    assert result.decisions[0].status == AgentDecisionStatus.PUBLISHED
    assert result.decisions[0].publish_reason_ko == decision.publish_reason_ko
    assert result.decisions[0].confidence_score == 0.82
    assert "OpenAI developer feed summary" in client.responses.last_input
    assert "chunk-0001" in client.responses.last_input
    assert "concrete developer tooling changes" in client.responses.last_input
    assert "ranking_reasons_ko" in client.responses.last_input
    assert "500~900자" in client.responses.last_input
    assert "2~3문단" in client.responses.last_input
    assert "첫 문장과 문단 구성을 고정하지 말고" in client.responses.last_input
    assert "'해당 글은', '이 글은' 같은 표현" in client.responses.last_input


def test_openai_agent_skips_candidate_when_decision_says_not_to_publish() -> None:
    client = FakeOpenAIClient(
        OpenAIArticleDecision(
            should_publish=False,
            reject_reason_ko="제공된 피드 정보만으로는 기술적 의미가 부족합니다.",
        )
    )
    agent = OpenAINewsEditorAgent(api_key=None, model="gpt-5-mini", client=client)

    result = agent.edit(make_enrichment_result())

    assert result.services[0].briefings == []
    assert result.decisions[0].status == AgentDecisionStatus.SKIPPED
    assert result.decisions[0].reject_reason_ko == (
        "제공된 피드 정보만으로는 기술적 의미가 부족합니다."
    )


def test_openai_agent_retries_when_structured_output_parse_fails() -> None:
    decision = OpenAIArticleDecision(
        should_publish=True,
        category="AI",
        importance_level="Medium",
        publish_reason_ko="개발자 업데이트로 볼 수 있습니다.",
        summary_ko="피드 기준으로 개발자 업데이트의 주요 내용을 정리합니다.",
    )
    client = RetryOpenAIClient(decision)
    agent = OpenAINewsEditorAgent(api_key=None, model="gpt-5-mini", client=client)

    result = agent.edit(make_enrichment_result())

    assert client.responses.calls == 2
    assert result.services[0].briefings[0].category == "AI"


def test_openai_agent_skips_candidate_when_structured_output_parse_keeps_failing() -> None:
    class AlwaysFailingResponses:
        calls = 0

        def parse(self, **kwargs):
            self.calls += 1
            raise ValueError("Invalid JSON: EOF while parsing a string")

    class AlwaysFailingOpenAIClient:
        def __init__(self) -> None:
            self.responses = AlwaysFailingResponses()

    client = AlwaysFailingOpenAIClient()
    agent = OpenAINewsEditorAgent(api_key=None, model="gpt-5-mini", client=client)

    result = agent.edit(make_enrichment_result())

    assert client.responses.calls == 2
    assert result.services[0].briefings == []
    assert result.decisions[0].status == AgentDecisionStatus.FAILED
    assert result.decisions[0].error_message


def test_openai_agent_skips_unselected_long_content_without_api_call() -> None:
    decision = OpenAIArticleDecision(should_publish=True)
    client = FakeOpenAIClient(decision)
    agent = OpenAINewsEditorAgent(api_key=None, model="gpt-5-mini", client=client)

    result = agent.edit(make_enrichment_result(strategy=EnrichmentInputStrategy.CHUNK_SELECTION))

    assert result.services[0].briefings == []
    assert result.decisions[0].status == AgentDecisionStatus.SKIPPED
    assert client.responses.last_input == ""


def test_openai_agent_publishes_selected_long_content() -> None:
    decision = OpenAIArticleDecision(
        should_publish=True,
        category="AI",
        importance_level="Medium",
        confidence_score=0.74,
        summary_scope="chunk_selection",
        publish_reason_ko="선택된 원문 근거가 개발자에게 의미 있는 변화를 설명합니다.",
        evidence_basis_ko=["chunk-0001"],
        summary_ko=(
            "선택된 원문 근거는 개발자 도구 변화와 적용 맥락을 중심으로 설명합니다. "
            "전체 원문을 모두 다루기보다는 제공된 근거 범위 안에서 핵심 변화를 정리합니다.\n\n"
            "이 업데이트는 도구 통합 흐름과 개발자 경험에 영향을 줄 수 있습니다. "
            "세부 범위는 원문에서 추가 확인이 필요합니다."
        ),
    )
    client = FakeOpenAIClient(decision)
    agent = OpenAINewsEditorAgent(api_key=None, model="gpt-5-mini", client=client)

    result = agent.edit(
        make_enrichment_result(
            strategy=EnrichmentInputStrategy.CHUNK_SELECTION,
            select_chunks=True,
        )
    )

    assert result.services[0].briefings[0].summary_scope == "chunk_selection"
    assert "source_evidence" in client.responses.last_input


def test_openai_agent_requires_api_key_without_injected_client() -> None:
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        OpenAINewsEditorAgent(api_key=None, model="gpt-5-mini")
