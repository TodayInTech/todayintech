from src.enrichment.extractors import HtmlContentExtractor
from src.enrichment.models import DocumentBlockType, FetchedContent
from src.enrichment.tokenization import TiktokenTokenCounter


def test_html_extractor_preserves_structural_blocks_without_duplicates() -> None:
    html = """
    <html>
      <head><title>Structured Agent Architecture</title></head>
      <body>
        <article>
          <h1>Structured Agent Architecture</h1>
          <p>This article explains a pipeline architecture for reliable agent systems.</p>
          <h2>Implementation</h2>
          <ul><li>Separate fetching and extraction.</li><li>Keep evidence traceable.</li></ul>
          <pre><code>run_pipeline()</code></pre>
        </article>
      </body>
    </html>
    """
    fetched = FetchedContent(
        source_url="https://example.com/article",
        final_url="https://example.com/article",
        http_status=200,
        content_type="text/html",
        body=html,
        response_bytes=len(html.encode()),
        duration_ms=10,
    )

    document = HtmlContentExtractor(TiktokenTokenCounter()).extract(fetched)

    assert document.title == "Structured Agent Architecture"
    assert document.token_count > 0
    assert document.content_hash
    assert [block.block_type for block in document.blocks] == [
        DocumentBlockType.HEADING,
        DocumentBlockType.PARAGRAPH,
        DocumentBlockType.HEADING,
        DocumentBlockType.LIST_ITEM,
        DocumentBlockType.LIST_ITEM,
        DocumentBlockType.CODE,
    ]
