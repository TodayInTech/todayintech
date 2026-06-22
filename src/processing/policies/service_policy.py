from pydantic import BaseModel

from src.processing.models import ArticleCandidate
from src.processing.policies.base import BasePreprocessingPolicy


class ServicePreprocessingPolicy(BaseModel, BasePreprocessingPolicy):
    service_key: str = "default"
    min_candidate_score: float = 12
    min_text_length: int = 12
    max_low_signal_count_without_high_signal: int = 1
    low_signal_reject_reason_ko: str = "홍보성 또는 이벤트성 신호가 강한 후보입니다."
    low_score_reject_reason_ko: str = "후보 점수가 서비스별 최소 기준에 미치지 못합니다."
    thin_text_reject_reason_ko: str = "제목과 피드 설명만으로는 브리핑 근거가 부족합니다."

    def reject_reason(self, candidate: ArticleCandidate) -> str | None:
        if candidate.candidate_score < self.min_candidate_score:
            return self.low_score_reject_reason_ko

        text_length = len(f"{candidate.article.title} {candidate.feed_summary}".strip())
        if text_length < self.min_text_length:
            return self.thin_text_reject_reason_ko

        signals = candidate.ranking_signals
        if (
            signals.low_signal_count > self.max_low_signal_count_without_high_signal
            and signals.high_signal_count == 0
        ):
            return self.low_signal_reject_reason_ko

        return None


class ServicePreprocessingPolicyRegistry:
    def __init__(
        self,
        policies: dict[str, ServicePreprocessingPolicy] | None = None,
        default_policy: ServicePreprocessingPolicy | None = None,
    ) -> None:
        self.default_policy = default_policy or ServicePreprocessingPolicy()
        self.policies = policies or default_service_policies()

    def get(self, service_key: str) -> ServicePreprocessingPolicy:
        return self.policies.get(service_key, self.default_policy)


def default_service_policies() -> dict[str, ServicePreprocessingPolicy]:
    return {
        "hacker-news": ServicePreprocessingPolicy(
            service_key="hacker-news",
            min_candidate_score=18,
            min_text_length=10,
        ),
        "github-blog": ServicePreprocessingPolicy(
            service_key="github-blog",
            min_candidate_score=20,
        ),
        "google-blog": ServicePreprocessingPolicy(
            service_key="google-blog",
            min_candidate_score=20,
            max_low_signal_count_without_high_signal=0,
        ),
        "openai-blog": ServicePreprocessingPolicy(
            service_key="openai-blog",
            min_candidate_score=20,
        ),
        "anthropic-blog": ServicePreprocessingPolicy(
            service_key="anthropic-blog",
            min_candidate_score=20,
        ),
    }
