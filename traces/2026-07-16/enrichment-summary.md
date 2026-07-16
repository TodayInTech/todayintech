# Enrichment Trace - 2026-07-16

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 120 ms
- Candidates: 9
- Usable candidates: 8 (88.9%)
- Writer-ready candidates: 7 (77.8%)
- Status counts: enriched: 6, failed: 1, fallback: 2
- Input strategies: chunk_selection: 1, feed_metadata_only: 2, full_content: 5, none: 1
- Failure reasons: access_denied: 3
- Extracted tokens: p50 784, p90 2556, max 4002

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 2 | 2 | 2 | 0 | 0 | 390 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1063 |
| openai-blog | 3 | 2 | 0 | 2 | 1 | 0 |
