from datetime import UTC, datetime

from src.processing.models import ArticleCandidate, RankingSignals
from src.processing.scoring.base import BaseCandidateScorer

HIGH_SIGNAL_KEYWORDS = (
    "agent",
    "api",
    "benchmark",
    "launch",
    "model",
    "open source",
    "release",
    "security",
    "vulnerability",
)
LOW_SIGNAL_KEYWORDS = (
    "event",
    "podcast",
    "roundup",
    "shop",
    "webinar",
)
SOURCE_PRIORITY = {
    "openai-blog": 10,
    "anthropic-blog": 10,
    "github-blog": 8,
    "google-blog": 7,
    "hacker-news": 5,
}


class DefaultCandidateScorer(BaseCandidateScorer):
    def score(self, candidate: ArticleCandidate, now: datetime | None = None) -> ArticleCandidate:
        reference_time = now or datetime.now(UTC)
        article = candidate.article
        text = f"{article.title} {article.summary or ''}".lower()
        signals = RankingSignals()
        score = 0.0

        source_score = SOURCE_PRIORITY.get(candidate.service_key, 3)
        signals.source_priority = source_score
        score += source_score

        if article.published_at:
            published_at = article.published_at
            if published_at.tzinfo is None:
                published_at = published_at.replace(tzinfo=UTC)

            age_days = max((reference_time - published_at).days, 0)
            freshness_score = max(0, 20 - min(age_days, 20))
            signals.age_days = age_days
            signals.freshness_score = freshness_score
            score += freshness_score

        high_signal_count = sum(1 for keyword in HIGH_SIGNAL_KEYWORDS if keyword in text)
        low_signal_count = sum(1 for keyword in LOW_SIGNAL_KEYWORDS if keyword in text)
        signals.high_signal_count = high_signal_count
        signals.low_signal_count = low_signal_count
        score += high_signal_count * 5
        score -= low_signal_count * 4

        hn_points = int(article.metadata.get("hn_points", 0))
        hn_comments = int(article.metadata.get("hn_comments", 0))
        rss_rank = int(article.metadata.get("rss_rank", 0))
        if hn_points:
            hn_points_score = min(hn_points / 10, 20)
            signals.hn_points_score = round(hn_points_score, 2)
            score += hn_points_score
        if hn_comments:
            hn_comments_score = min(hn_comments / 5, 15)
            signals.hn_comments_score = round(hn_comments_score, 2)
            score += hn_comments_score
        if rss_rank:
            rank_score = max(0, 10 - min(rss_rank, 10))
            signals.rss_rank_score = rank_score
            score += rank_score

        return candidate.model_copy(
            update={
                "candidate_score": round(score, 2),
                "ranking_signals": signals,
            }
        )
