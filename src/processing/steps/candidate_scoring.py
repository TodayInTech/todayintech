from datetime import UTC, datetime, time

from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.scoring import BaseCandidateScorer, DefaultCandidateScorer


class CandidateScoringStep(BasePreprocessingStep):
    name = "candidate_scoring"

    def __init__(self, scorer: BaseCandidateScorer | None = None) -> None:
        self.scorer = scorer or DefaultCandidateScorer()

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        reference_time = _reference_time(context.generated_for)
        context.replace_candidates(
            [
                self.scorer.score(candidate, now=reference_time)
                for candidate in sorted(
                    context.candidates,
                    key=lambda item: item.article.published_at or datetime.min.replace(tzinfo=UTC),
                    reverse=True,
                )
            ]
        )
        return context


def _reference_time(generated_for: str) -> datetime:
    try:
        target_date = datetime.fromisoformat(generated_for).date()
    except ValueError:
        return datetime.now(UTC)
    return datetime.combine(target_date, time.min, tzinfo=UTC)
