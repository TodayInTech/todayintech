from collections import defaultdict

from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.enums import ExcludedReason
from src.processing.models import ArticleCandidate


class CandidateLimitStep(BasePreprocessingStep):
    name = "candidate_limiting"

    def __init__(self, per_service_limit: int, total_limit: int) -> None:
        self.per_service_limit = per_service_limit
        self.total_limit = total_limit

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        by_service_count: dict[str, int] = defaultdict(int)
        kept: list[ArticleCandidate] = []

        for candidate in sorted(
            context.candidates,
            key=lambda item: item.candidate_score,
            reverse=True,
        ):
            if by_service_count[candidate.service_key] >= self.per_service_limit:
                context.exclude_candidate(candidate, ExcludedReason.SERVICE_CANDIDATE_LIMIT)
                context.increment_stat("limit_removed")
                continue
            if len(kept) >= self.total_limit:
                context.exclude_candidate(candidate, ExcludedReason.TOTAL_CANDIDATE_LIMIT)
                context.increment_stat("limit_removed")
                continue
            by_service_count[candidate.service_key] += 1
            kept.append(candidate)

        context.replace_candidates(kept)
        return context
