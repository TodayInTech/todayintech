# Enrichment Trace - 2026-07-17

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 48 ms
- Candidates: 7
- Usable candidates: 6 (85.7%)
- Writer-ready candidates: 6 (85.7%)
- Status counts: enriched: 5, failed: 1, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 5, none: 1
- Failure reasons: access_denied: 2
- Extracted tokens: p50 1435, p90 2129, max 2510

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1435 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1108 |
| openai-blog | 2 | 1 | 0 | 1 | 1 | 0 |
