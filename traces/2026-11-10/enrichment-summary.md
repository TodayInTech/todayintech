# Enrichment Trace - 2026-11-10

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 284 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 4, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 4
- Failure reasons: access_denied: 5
- Extracted tokens: p50 1672, p90 2443, max 2658

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 1 | 1 | 1 | 0 | 0 | 169 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1941 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
