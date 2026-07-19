# Enrichment Trace - 2026-07-19

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 40212 ms
- Candidates: 5
- Usable candidates: 4 (80.0%)
- Writer-ready candidates: 4 (80.0%)
- Status counts: enriched: 3, failed: 1, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 3, none: 1
- Failure reasons: access_denied: 1, fetch_timeout: 1
- Extracted tokens: p50 732, p90 819, max 841

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 732 |
| openai-blog | 1 | 0 | 0 | 0 | 1 | 0 |
