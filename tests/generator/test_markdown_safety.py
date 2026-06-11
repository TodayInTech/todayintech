from datetime import UTC, datetime

from src.generator.markdown_safety import mdx_safe_plain_text, mdx_safe_text
from src.generator.service_markdown_writer import write_service_markdown
from src.models import Article, ArticleSummary, NewsCategory, ServiceBriefing


def test_mdx_safe_text_strips_html_and_escapes_mdx_tokens() -> None:
    text = mdx_safe_text('<p>Article <a href="https://example.com">URL</a> {x}</p>')

    assert "<p>" not in text
    assert "<a" not in text
    assert "Article URL &#123;x&#125;" in text


def test_mdx_safe_plain_text_preserves_angle_brackets_as_text() -> None:
    text = mdx_safe_plain_text("A <tag> title {draft}")

    assert text == "A &lt;tag&gt; title &#123;draft&#125;"


def test_mdx_safe_text_escapes_markdown_block_markers() -> None:
    text = mdx_safe_text("<p># Comments: 12</p><p>- item</p>")

    assert "\\# Comments: 12" in text
    assert "\\- item" in text


def test_service_markdown_writer_outputs_mdx_safe_external_content(tmp_path) -> None:
    article = Article(
        source="Hacker News",
        title="A <tag> title {draft}",
        url="https://example.com/post",
        collected_at=datetime.now(UTC),
        summary='<p>Article URL: <a href="https://example.com/post">link</a></p>',
    )
    summary = ArticleSummary(
        article=article,
        category=NewsCategory.DEVELOPER_TOOLS,
        importance_score=4,
        importance_reason="test",
        summary_ko=article.summary or "",
        why_it_matters_ko="Uses {agent} metadata",
    )
    briefing = ServiceBriefing(
        service_key="hacker-news",
        service_name="Hacker News",
        generated_for="2026-06-11",
        summaries=[summary],
    )

    output_path = write_service_markdown(tmp_path, briefing)
    content = output_path.read_text(encoding="utf-8")

    assert "<p>" not in content
    assert "<a" not in content
    assert "### A &lt;tag&gt; title &#123;draft&#125;" in content
    assert "Article URL: link" in content
    assert "Uses &#123;agent&#125; metadata" in content
