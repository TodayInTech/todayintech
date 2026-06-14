from src.processing.briefed_article_store import BriefedArticleStore


def test_briefed_article_store_matches_by_url(tmp_path) -> None:
    store = BriefedArticleStore(tmp_path / "briefed_articles.json")
    store.mark_published(
        normalized_url="https://example.com/post",
        title_fingerprint="example post",
        service_key="github-blog",
        title="Example Post",
    )
    store.save()

    reloaded = BriefedArticleStore(tmp_path / "briefed_articles.json")

    assert reloaded.contains(
        "https://example.com/post",
        "different title",
        "github-blog",
    )


def test_briefed_article_store_matches_title_within_same_service(tmp_path) -> None:
    store = BriefedArticleStore(tmp_path / "briefed_articles.json")
    store.mark_published(
        normalized_url="https://example.com/original",
        title_fingerprint="same title",
        service_key="openai-blog",
        title="Same Title",
    )

    assert store.contains(
        "https://example.com/canonical-changed",
        "same title",
        "openai-blog",
    )
    assert not store.contains(
        "https://example.com/canonical-changed",
        "same title",
        "github-blog",
    )


def test_briefed_article_store_treats_draft_as_active_written_article(tmp_path) -> None:
    store = BriefedArticleStore(tmp_path / "briefed_articles.json")
    store.mark_draft(
        normalized_url="https://example.com/draft",
        title_fingerprint="draft article",
        service_key="hacker-news",
        title="Draft Article",
        article_doc_path="docs/services/hacker-news/draft.md",
    )

    assert store.contains(
        "https://example.com/draft",
        "draft article",
        "hacker-news",
    )
