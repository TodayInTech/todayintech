from datetime import UTC, datetime

from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.scoring import BaseCandidateScorer, DefaultCandidateScorer


class CandidateScoringStep(BasePreprocessingStep):
    name = "candidate_scoring"

    def __init__(self, scorer: BaseCandidateScorer | None = None) -> None:
        self.scorer = scorer or DefaultCandidateScorer()

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        context.replace_candidates(
            [
                self.scorer.score(candidate)
                for candidate in sorted(
                    context.candidates,
                    key=lambda item: item.article.published_at or datetime.min.replace(tzinfo=UTC),
                    reverse=True,
                )
            ]
        )
        return context
