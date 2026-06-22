from src.tracing.writer_trace import build_writer_decision_trace, write_writer_decision_trace
from src.writer.agent.schemas import AgentDecision, AgentDecisionStatus, GenerationMethod


def make_decision(status: AgentDecisionStatus = AgentDecisionStatus.PUBLISHED) -> AgentDecision:
    return AgentDecision(
        candidate_id="openai-blog:abc123",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        title="OpenAI Developer Update",
        normalized_url="https://openai.com/news/update",
        article_doc_path="docs/services/openai-blog/openai-developer-update.md",
        status=status,
        generation_method=GenerationMethod.LLM,
        category="AI",
        importance_level="High",
        confidence_score=0.82,
        summary_scope="feed_metadata_only",
        publish_reason_ko="개발자 워크플로에 영향을 줄 수 있는 업데이트입니다.",
        evidence_basis_ko=["피드 설명이 개발자 업데이트를 언급합니다."],
        candidate_score=42,
    )


def test_build_writer_decision_trace_counts_decisions() -> None:
    trace = build_writer_decision_trace(
        generated_for="2026-06-11",
        agent_name="openai",
        decisions=[
            make_decision(AgentDecisionStatus.PUBLISHED),
            make_decision(AgentDecisionStatus.SKIPPED),
        ],
    )

    assert trace["stage"] == "writer"
    assert trace["agent"] == "openai"
    assert trace["decision_count"] == 2
    assert trace["decision_counts"] == {"published": 1, "skipped": 1}
    assert trace["decisions"][0]["summary_scope"] == "feed_metadata_only"


def test_write_writer_decision_trace_outputs_json_and_markdown(tmp_path) -> None:
    written_paths = write_writer_decision_trace(
        tmp_path,
        generated_for="2026-06-11",
        agent_name="openai",
        decisions=[make_decision()],
    )

    assert tmp_path.joinpath("2026-06-11", "writer-decisions.json") in written_paths
    assert tmp_path.joinpath("2026-06-11", "writer-decisions-summary.md") in written_paths
    assert tmp_path.joinpath("2026-06-11", "writer-decisions.json").exists()
    assert tmp_path.joinpath("2026-06-11", "writer-decisions-summary.md").exists()
