from datetime import UTC, datetime

from src.generator.markdown_safety import mdx_safe_article, mdx_safe_plain_text, mdx_safe_text
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


def test_article_markdown_preserves_structure_and_code_without_executing_mdx() -> None:
    body = """도입 문단입니다.

## 달라진 API

- **버전 2 지원**

| 이전 | 이후 |
| --- | --- |
| v1 | v2 |

> 원문의 짧은 발언

`Map<string, int>`와 {alert(1)} <Widget />

```js
const config = {value: "<script>"};
```

export const unsafe = 1
import Thing from './x'
[클릭](javascript:alert(1))
"""
    rendered = mdx_safe_article(body)
    assert "## 달라진 API\n\n- **버전 2 지원**" in rendered
    assert "| 이전 | 이후 |" in rendered
    assert "> 원문의 짧은 발언" in rendered
    assert "`Map<string, int>`" in rendered
    assert 'const config = {value: "<script>"};' in rendered
    assert "&#123;alert(1)&#125; &lt;Widget /&gt;" in rendered
    assert "&#101;xport" in rendered and "&#105;mport" in rendered
    assert r"\[클릭\](javascript:" in rendered


def test_article_markdown_handles_escaped_code_links_and_unclosed_fences() -> None:
    rendered = mdx_safe_article(r"\`{alert(1)}` \[click\](javascript:alert(1))")
    assert "&#123;alert(1)&#125;" in rendered
    assert r"\\\[click\\\]" in rendered
    assert mdx_safe_article("```py\nx = {'a': 1}").endswith("\n```")
    assert mdx_safe_article("# Duplicate title").startswith("## Duplicate")
    assert mdx_safe_article("```js {bad}\n{}\n```") == "```js\n{}\n```"
