# Dynamic article generation verification

The collection/preprocessing/enrichment/writer/site pipeline, article identity and deduplication state remain unchanged. The Writer adds `article_markdown_ko` for detailed Markdown; `summary_ko` remains a short list summary stored in standard `description` frontmatter. Legacy pages retain paragraph-based excerpts and drafts retain their existing output.

## Live model comparison

The same cached source chunks from 2026-06-13 were sent to the old and final improved prompts using `gpt-5-mini`, without increasing input/output token budgets. Counts include spaces and Markdown. These are one final-prompt sample per candidate, not averages over prompt iterations; generation is nondeterministic.

| Article | Evidence tokens | Old characters | New characters | New headings | Exact duplicate sentences |
| --- | ---: | ---: | ---: | ---: | ---: |
| Making secret scanning more trustworthy: Reducing false positives at scale | 1083 | 749 | 1401 | 4 | 0 |
| DiffusionGemma: 4x faster text generation | 1271 | 1011 | 1784 | 5 | 0 |
| Access OpenAI models and Codex through your Oracle cloud commitment | 262 | 639 | 753 | 0 | 0 |

## Evidence review and limits

The GitHub sample preserves verification-only pipeline changes, focused usage context, a 65% target and 75.76% false-positive reduction on hundreds of customer-confirmed false positives. Author biographies and the unrelated Qubot teaser are not treated as participants in the work. The Google sample retains 26B/3.8B parameters, 256-token parallel generation, up-to-4x claims, hardware-specific throughput, quantized 18GB VRAM, lower quality than Gemma 4, low-concurrency tradeoffs and future llama.cpp support. These are source claims, not independently reproduced benchmarks. The Oracle sample preserves eligible credits and relative availability without inventing dates, model versions, prices, authentication APIs or security guarantees. Final evidence IDs resolve to the supplied chunks.

Exact sentence duplication was zero; this does not establish semantic uniqueness or factual correctness. The short procurement sample still partially restates the purchasing-path significance, so human sampling remains necessary. Three examples do not establish platform-wide accuracy.

Existing Enrichment supplies full sources up to 4,000 tokens and selects up to 4,000 tokens for longer pages. These samples had 262–1,271 full-content tokens and contained sufficient facts without additional collection. Sparse/feed-only evidence must stay brief; no selected evidence still prevents publication. The extractor records code/table/list block types but does not fully preserve code indentation/newlines or table cell boundaries. Do not reconstruct code when exact syntax is unavailable; code-heavy stories need separate extraction-quality review. Collection/extraction and token budgets were unchanged.

## Rendering

Preserve optional headings, lists, tables, quotes and literal code; render raw HTML, MDX expressions and import/export as inert text. Model-generated links/images are disabled and the generator adds the canonical source link. See the [actual Korean generated example](../../../harness/examples/dynamic-article.md) and [Korean verification report](../../../harness/ARTICLE_GENERATION.md). Examples are not registered in production article or deduplication state.
