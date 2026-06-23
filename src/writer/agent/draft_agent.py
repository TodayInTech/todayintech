from collections import defaultdict

from src.enrichment.models import EnrichedArticleCandidate, EnrichmentResult
from src.processing.models import ArticleCandidate
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
    def edit(self, enrichment_result: EnrichmentResult) -> EditorialResult:
        total_candidates = len(enrichment_result.candidates)
        log_info("Draft Agent", f"draft briefing 생성: candidates={total_candidates}")
        decisions = [
            self._create_draft_decision(enriched.candidate)
            for enriched in enrichment_result.candidates
        ]
        candidates_by_service: dict[str, list[EnrichedArticleCandidate]] = defaultdict(list)
        for enriched in enrichment_result.candidates:
            candidates_by_service[enriched.candidate.service_key].append(enriched)
        service_names = dict(enrichment_result.service_names)
        for enriched in enrichment_result.candidates:
            service_names.setdefault(
                enriched.candidate.service_key,
                enriched.candidate.service_name,
            )
        return EditorialResult(
            generated_for=enrichment_result.generated_for,
            decisions=decisions,
            services=[
                ServiceWritingResult(
                    service_key=service_key,
                    service_name=service_names[service_key],
                    briefings=[
                        self._create_draft_briefing(enriched.candidate)
                        for enriched in enriched_candidates
                    ],
                )
                for service_key in sorted(service_names)
                for enriched_candidates in [candidates_by_service.get(service_key, [])]
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
