# Enrichment Trace - 2026-11-15

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 230 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 10 (100.0%)
- Status counts: enriched: 8, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 8
- Failure reasons: access_denied: 1, extraction_failed: 1
- Extracted tokens: p50 1092, p90 1727, max 2281

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1044 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1133 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1379 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
