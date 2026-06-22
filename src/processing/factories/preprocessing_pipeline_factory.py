from src.processing.contracts import BasePreprocessingStep
from src.processing.state import BriefedArticleStore
from src.processing.steps import (
    BriefedArticleFilterStep,
    CandidateIdentityStep,
    CandidateLimitStep,
    CandidateScoringStep,
    RunDeduplicationStep,
    UrlNormalizationStep,
    ValidationStep,
)


class PreprocessingPipelineFactory:
    """Build ordered preprocessing step pipelines."""

    def create_default(
        self,
        *,
        briefed_article_store: BriefedArticleStore,
        per_service_limit: int,
        total_limit: int,
    ) -> list[BasePreprocessingStep]:
        return [
            ValidationStep(),
            UrlNormalizationStep(),
            CandidateIdentityStep(),
            RunDeduplicationStep(),
            BriefedArticleFilterStep(briefed_article_store),
            CandidateScoringStep(),
            CandidateLimitStep(per_service_limit, total_limit),
        ]
