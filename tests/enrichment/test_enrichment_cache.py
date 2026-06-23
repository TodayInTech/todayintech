from datetime import UTC, datetime

from src.enrichment.models import (
    EnrichedArticleCandidate,
    EnrichmentInputStrategy,
    EnrichmentStatus,
)
from src.enrichment.state import JsonEnrichmentCache
from src.models import Article
from src.processing.models import ArticleCandidate


def make_candidate() -> ArticleCandidate:
    return ArticleCandidate(
        candidate_id="openai-blog:abc",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        normalized_url="https://openai.com/index/agent",
        article=Article(
            source="OpenAI Blog",
            title="Agent Architecture",
            url="https://openai.com/index/agent",
            collected_at=datetime(2026, 6, 23, tzinfo=UTC),
        ),
    )


def test_json_enrichment_cache_uses_versioned_key_and_round_trips(tmp_path) -> None:
    cache = JsonEnrichmentCache(tmp_path)
    candidate = make_candidate()
    key = cache.build_key(
        candidate,
        extractor_name="trafilatura",
        extractor_version="2.1.0",
        chunker_name="structural:max=1200",
        policy_name="adaptive-token-budget",
        policy_version="1",
    )
    result = EnrichedArticleCandidate(
        candidate=candidate,
        status=EnrichmentStatus.ENRICHED,
        input_strategy=EnrichmentInputStrategy.FULL_CONTENT,
    )

    cache.save(key, result)

    assert cache.get(key) == result
    assert (
        cache.build_key(
            candidate,
            extractor_name="trafilatura",
            extractor_version="2.2.0",
            chunker_name="structural:max=1200",
            policy_name="adaptive-token-budget",
            policy_version="1",
        )
        != key
    )
    assert (
        cache.build_key(
            candidate,
            extractor_name="trafilatura",
            extractor_version="2.1.0",
            chunker_name="structural:max=800",
            policy_name="adaptive-token-budget",
            policy_version="1",
        )
        != key
    )
