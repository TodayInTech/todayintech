from pydantic import BaseModel, Field

from src.models import ServiceCollectionResult
from src.processing.enums import ExcludedReason
from src.processing.models import ArticleCandidate, PreprocessingStepMetrics


class PreprocessingContext(BaseModel):
    generated_for: str
    collection_results: list[ServiceCollectionResult]
    candidates: list[ArticleCandidate] = Field(default_factory=list)
    excluded: list[ArticleCandidate] = Field(default_factory=list)
    stats: dict[str, int] = Field(default_factory=dict)
    step_metrics: list[PreprocessingStepMetrics] = Field(default_factory=list)

    def add_candidate(self, candidate: ArticleCandidate) -> None:
        self.candidates.append(candidate)

    def replace_candidates(self, candidates: list[ArticleCandidate]) -> None:
        self.candidates = candidates

    def exclude_candidate(
        self,
        candidate: ArticleCandidate,
        reason: ExcludedReason,
    ) -> None:
        self.excluded.append(candidate.model_copy(update={"excluded_reason": reason}))

    def increment_stat(self, key: str, amount: int = 1) -> None:
        self.stats[key] = self.stats.get(key, 0) + amount

    def add_step_metrics(self, metrics: PreprocessingStepMetrics) -> None:
        self.step_metrics.append(metrics)
