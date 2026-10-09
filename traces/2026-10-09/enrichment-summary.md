# Enrichment Trace - 2026-10-09

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 818 ms
- Candidates: 15
- Usable candidates: 15 (100.0%)
- Writer-ready candidates: 14 (93.3%)
- Status counts: enriched: 10, fallback: 5
- Input strategies: chunk_selection: 1, feed_metadata_only: 5, full_content: 9
- Failure reasons: access_denied: 4, thin_content: 1
- Extracted tokens: p50 1344, p90 3129, max 6698

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 3 | 3 | 3 | 0 | 0 | 1404 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1285 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 263 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2408 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
