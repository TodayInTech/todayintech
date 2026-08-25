# Enrichment Trace - 2026-08-25

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 812 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 13 (92.9%)
- Status counts: enriched: 8, fallback: 6
- Input strategies: chunk_selection: 1, feed_metadata_only: 6, full_content: 7
- Failure reasons: access_denied: 4, extraction_failed: 1, thin_content: 1
- Extracted tokens: p50 1930, p90 3899, max 5864

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1564 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 3057 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 754 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 3826 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
