from datetime import UTC, datetime

from src.models import Article
from src.processing.candidate_identity import (
    candidate_id,
    slugify_title,
    suggested_article_path,
    suggested_doc_key,
    url_hash,
)


def make_article() -> Article:
    return Article(
        source="OpenAI Blog",
        title="Access OpenAI models and Codex through your Oracle cloud commitment",
        url="https://openai.com/index/openai-on-oracle-cloud",
        published_at=datetime(2026, 6, 10, tzinfo=UTC),
        collected_at=datetime(2026, 6, 11, tzinfo=UTC),
    )


def test_candidate_identity_uses_stable_url_hash() -> None:
    normalized_url = "https://openai.com/index/openai-on-oracle-cloud"

    assert len(url_hash(normalized_url)) == 64
    assert candidate_id("openai-blog", normalized_url).startswith("openai-blog:")


def test_suggested_doc_key_includes_date_slug_and_short_hash() -> None:
    normalized_url = "https://openai.com/index/openai-on-oracle-cloud"
    doc_key = suggested_doc_key(make_article(), normalized_url)

    assert doc_key.startswith("2026-06-access-openai-models-and-codex")
    assert doc_key.endswith(url_hash(normalized_url)[:8])
    assert suggested_article_path("openai-blog", doc_key) == (
        f"docs/articles/openai-blog/{doc_key}.md"
    )


def test_slugify_title_falls_back_for_non_ascii_title() -> None:
    assert slugify_title("기술 뉴스") == "article"
