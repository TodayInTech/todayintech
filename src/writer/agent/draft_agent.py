from src.processing.models import ArticleCandidate, PreprocessingResult
from src.progress import log_info
from src.writer.agent.schemas import (
    AgentDecision,
    AgentDecisionStatus,
    ArticleBriefing,
    EditorialResult,
    EditorialStatus,
    GenerationMethod,
    ServiceWritingResult,
)


class DraftNewsEditorAgent:
    def edit(self, preprocessing_result: PreprocessingResult) -> EditorialResult:
        total_candidates = sum(len(service.candidates) for service in preprocessing_result.services)
        log_info("Draft Agent", f"draft briefing 생성: candidates={total_candidates}")
        decisions = [
            self._create_draft_decision(candidate)
            for service in preprocessing_result.services
            for candidate in service.candidates
        ]
        return EditorialResult(
            generated_for=preprocessing_result.generated_for,
            decisions=decisions,
            services=[
                ServiceWritingResult(
                    service_key=service.service_key,
                    service_name=service.service_name,
                    briefings=[
                        self._create_draft_briefing(candidate) for candidate in service.candidates
                    ],
                )
                for service in preprocessing_result.services
            ],
        )

    def _create_draft_decision(self, candidate: ArticleCandidate) -> AgentDecision:
        return AgentDecision(
            candidate_id=candidate.candidate_id,
            service_key=candidate.service_key,
            service_name=candidate.service_name,
            title=candidate.article.title,
            normalized_url=candidate.normalized_url,
            article_doc_path=candidate.suggested_article_path,
            status=AgentDecisionStatus.DRAFT,
            generation_method=GenerationMethod.DRAFT,
            candidate_score=candidate.candidate_score,
        )

    def _create_draft_briefing(self, candidate: ArticleCandidate) -> ArticleBriefing:
        article = candidate.article
        return ArticleBriefing(
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
            editorial_status=EditorialStatus.DRAFT,
            generation_method=GenerationMethod.DRAFT,
        )
