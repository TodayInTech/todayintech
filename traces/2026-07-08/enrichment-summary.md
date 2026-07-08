# Enrichment Trace - 2026-07-08

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 343 ms
- Candidates: 15
- Usable candidates: 14 (93.3%)
- Writer-ready candidates: 14 (93.3%)
- Status counts: enriched: 10, failed: 1, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 10, none: 1
- Failure reasons: access_denied: 4, extraction_failed: 1
- Extracted tokens: p50 1708, p90 3125, max 3777

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1708 |
| github-blog | 3 | 3 | 3 | 0 | 0 | 2250 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1342 |
| openai-blog | 4 | 3 | 0 | 3 | 1 | 0 |
