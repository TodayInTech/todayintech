from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.enums import ExcludedReason
from src.processing.models import ArticleCandidate
from src.processing.policies import ServicePreprocessingPolicyRegistry


class CandidateQualityGateStep(BasePreprocessingStep):
    name = "candidate_quality_gate"

    def __init__(
        self,
        policy_registry: ServicePreprocessingPolicyRegistry | None = None,
    ) -> None:
        self.policy_registry = policy_registry or ServicePreprocessingPolicyRegistry()

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        kept: list[ArticleCandidate] = []

        for candidate in context.candidates:
            policy = self.policy_registry.get(candidate.service_key)
            reject_reason = policy.reject_reason(candidate)
            if reject_reason:
                context.exclude_candidate(
                    candidate.model_copy(
                        update={
                            "ranking_reasons_ko": [
                                *candidate.ranking_reasons_ko,
                                reject_reason,
                            ]
                        }
                    ),
                    ExcludedReason.LOW_QUALITY,
                )
                context.increment_stat("quality_gate_removed")
                continue
            kept.append(candidate)

        context.replace_candidates(kept)
        return context
