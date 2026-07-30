# Enrichment Trace - 2026-07-30

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 315 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 9, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 9
- Failure reasons: access_denied: 1, thin_content: 1
- Extracted tokens: p50 1808, p90 2274, max 3158

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 2006 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1723 |
| google-blog | 2 | 2 | 1 | 1 | 0 | 1433 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1808 |
