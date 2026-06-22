import json

from openai import OpenAI
from pydantic import ValidationError

from src.generator.markdown_safety import normalize_markdown_text
from src.processing.models import ArticleCandidate, PreprocessingResult
from src.progress import log_info
from src.writer.agent.schemas import (
    AgentDecision,
    AgentDecisionStatus,
    ArticleBriefing,
    EditorialResult,
    EditorialStatus,
    GenerationMethod,
    OpenAIArticleDecision,
    ServiceWritingResult,
)

SYSTEM_INSTRUCTIONS = """
You are the News Editor Agent for Today in Tech.

Write Korean editorial briefings from the provided candidate metadata only.
Do not claim that you read the full source article.
Do not invent details that are not present in the title, feed summary, tags, metadata, or ranking signals.
If information is limited, say so in Korean using phrasing like "피드 기준으로는" or "제공된 정보만 보면".

The article page should read like a short editorial briefing, not a rigid report.
Use a natural Korean briefing body, then concise key points, why it is worth reading, and caveats.
Reject candidates that are too thin, purely promotional, or not useful for technical readers.
""".strip()


class OpenAINewsEditorAgent:
    def __init__(
        self,
        *,
        api_key: str | None,
        model: str,
        client: OpenAI | None = None,
        max_output_tokens: int = 4096,
        retry_max_output_tokens: int = 6144,
    ) -> None:
        if client is None and not api_key:
            raise ValueError("OPENAI_API_KEY is required when TODAYINTECH_WRITER_AGENT=openai")

        self.client = client or OpenAI(api_key=api_key)
        self.model = model
        self.max_output_tokens = max_output_tokens
        self.retry_max_output_tokens = retry_max_output_tokens

    def edit(self, preprocessing_result: PreprocessingResult) -> EditorialResult:
        services: list[ServiceWritingResult] = []
        decisions: list[AgentDecision] = []
        total_candidates = sum(len(service.candidates) for service in preprocessing_result.services)
        processed_count = 0
        published_count = 0
        log_info(
            "OpenAI Agent", f"후보 검토 시작: candidates={total_candidates}, model={self.model}"
        )
        for service in preprocessing_result.services:
            briefings: list[ArticleBriefing] = []
            for candidate in service.candidates:
                processed_count += 1
                log_info(
                    "OpenAI Agent",
                    (
                        f"({processed_count}/{total_candidates}) 후보 검토 시작: "
                        f"{candidate.service_key} / {candidate.article.title}"
                    ),
                )
                briefing, agent_decision = self._review_candidate(candidate)
                decisions.append(agent_decision)
                if briefing is not None:
                    published_count += 1
                    log_info(
                        "OpenAI Agent",
                        (
                            f"({processed_count}/{total_candidates}) 게시 결정: "
                            f"category={briefing.category}, importance={briefing.importance_level}"
                        ),
                    )
                    briefings.append(briefing)
                else:
                    log_info(
                        "OpenAI Agent",
                        f"({processed_count}/{total_candidates}) 제외 결정",
                    )

            services.append(
                ServiceWritingResult(
                    service_key=service.service_key,
                    service_name=service.service_name,
                    briefings=briefings,
                )
            )

        log_info(
            "OpenAI Agent",
            f"후보 검토 완료: reviewed={processed_count}, published={published_count}",
        )
        return EditorialResult(
            generated_for=preprocessing_result.generated_for,
            services=services,
            decisions=decisions,
        )

    def _review_candidate(
        self,
        candidate: ArticleCandidate,
    ) -> tuple[ArticleBriefing | None, AgentDecision]:
        decision, error_message = self._parse_decision(candidate)
        if decision is None:
            return None, self._agent_decision(
                candidate,
                status=AgentDecisionStatus.FAILED,
                error_message=error_message or "structured output 파싱 재시도 실패",
            )

        if not decision.should_publish:
            return None, self._agent_decision(
                candidate,
                status=AgentDecisionStatus.SKIPPED,
                decision=decision,
            )

        article = candidate.article
        briefing = ArticleBriefing(
            candidate_id=candidate.candidate_id,
            service_key=candidate.service_key,
            service_name=candidate.service_name,
            title=article.title,
            source_url=str(article.url),
            normalized_url=candidate.normalized_url,
            title_fingerprint=candidate.title_fingerprint,
            published_at=article.published_at,
            collected_at=article.collected_at,
            feed_summary=candidate.feed_summary,
            candidate_score=candidate.candidate_score,
            ranking_signals=candidate.ranking_signals,
            ranking_reasons_ko=candidate.ranking_reasons_ko,
            suggested_doc_key=candidate.suggested_doc_key,
            article_doc_path=candidate.suggested_article_path,
            editorial_status=EditorialStatus.PUBLISHED,
            generation_method=GenerationMethod.LLM,
            category=decision.category,
            importance_level=decision.importance_level,
            confidence_score=decision.confidence_score,
            summary_scope=decision.summary_scope,
            publish_reason_ko=decision.publish_reason_ko,
            reject_reason_ko=decision.reject_reason_ko,
            evidence_basis_ko=decision.evidence_basis_ko,
            briefing_body_ko=decision.briefing_body_ko,
            key_points_ko=decision.key_points_ko,
            why_it_matters_ko=decision.why_it_matters_ko,
            caveats_ko=decision.caveats_ko,
        )
        return briefing, self._agent_decision(
            candidate,
            status=AgentDecisionStatus.PUBLISHED,
            decision=decision,
        )

    def _parse_decision(
        self,
        candidate: ArticleCandidate,
    ) -> tuple[OpenAIArticleDecision | None, str | None]:
        prompt = self._candidate_prompt(candidate)
        token_limits = [self.max_output_tokens, self.retry_max_output_tokens]
        last_error: str | None = None
        for attempt, max_output_tokens in enumerate(token_limits, start=1):
            try:
                response = self.client.responses.parse(
                    model=self.model,
                    instructions=SYSTEM_INSTRUCTIONS,
                    input=prompt,
                    text_format=OpenAIArticleDecision,
                    max_output_tokens=max_output_tokens,
                )
            except (ValidationError, ValueError) as exc:
                log_info(
                    "OpenAI Agent",
                    (
                        "structured output 파싱 실패: "
                        f"candidate_id={candidate.candidate_id}, "
                        f"attempt={attempt}/{len(token_limits)}, "
                        f"max_output_tokens={max_output_tokens}, "
                        f"error={exc}"
                    ),
                )
                last_error = str(exc)
                continue

            return response.output_parsed, None

        log_info(
            "OpenAI Agent",
            f"후보 제외: structured output 파싱 재시도 실패 candidate_id={candidate.candidate_id}",
        )
        return None, last_error

    def _agent_decision(
        self,
        candidate: ArticleCandidate,
        *,
        status: AgentDecisionStatus,
        decision: OpenAIArticleDecision | None = None,
        error_message: str | None = None,
    ) -> AgentDecision:
        return AgentDecision(
            candidate_id=candidate.candidate_id,
            service_key=candidate.service_key,
            service_name=candidate.service_name,
            title=candidate.article.title,
            normalized_url=candidate.normalized_url,
            article_doc_path=candidate.suggested_article_path,
            status=status,
            generation_method=GenerationMethod.LLM,
            category=decision.category if decision else None,
            importance_level=decision.importance_level if decision else None,
            confidence_score=decision.confidence_score if decision else None,
            summary_scope=decision.summary_scope if decision else None,
            publish_reason_ko=decision.publish_reason_ko if decision else None,
            reject_reason_ko=decision.reject_reason_ko if decision else None,
            evidence_basis_ko=decision.evidence_basis_ko if decision else [],
            candidate_score=candidate.candidate_score,
            error_message=error_message,
        )

    def _candidate_prompt(self, candidate: ArticleCandidate) -> str:
        article = candidate.article
        payload = {
            "candidate_id": candidate.candidate_id,
            "service_key": candidate.service_key,
            "service_name": candidate.service_name,
            "title": article.title,
            "source_url": str(article.url),
            "normalized_url": candidate.normalized_url,
            "published_at": article.published_at.isoformat() if article.published_at else None,
            "collected_at": article.collected_at.isoformat(),
            "feed_summary": truncate_text(normalize_markdown_text(candidate.feed_summary), 2000),
            "authors": article.authors,
            "tags": article.tags,
            "metadata": article.metadata,
            "candidate_score": candidate.candidate_score,
            "ranking_signals": candidate.ranking_signals.compact_dict(),
            "ranking_reasons_ko": candidate.ranking_reasons_ko,
        }
        return (
            "다음 JSON 후보를 검토해서 Today in Tech에 게시할 브리핑을 작성하세요.\n"
            "게시 가치가 낮으면 should_publish=false를 반환하세요.\n"
            "summary_scope는 현재 제공된 후보 메타데이터만 사용하므로 feed_metadata_only로 설정하세요.\n"
            "confidence_score는 0.0~1.0 사이로 판단 확신도를 표시하세요.\n"
            "publish_reason_ko 또는 reject_reason_ko 중 결정에 맞는 필드를 채우세요.\n"
            "evidence_basis_ko에는 제목, 피드 설명, 메타데이터, ranking signal 중 실제 판단 근거만 적으세요.\n"
            "게시한다면 briefing_body_ko는 자연스러운 한국어 2문단 이내로 작성하세요.\n"
            "key_points_ko는 2~3개, caveats_ko는 정보 한계나 원문 확인 필요사항 1~2개로 작성하세요.\n"
            "각 문장은 짧고 명확하게 작성하세요.\n\n"
            f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
        )


def truncate_text(value: str, max_length: int) -> str:
    if len(value) <= max_length:
        return value
    return value[: max_length - 1].rstrip() + "…"
