# Enrichment Trace - 2026-10-29

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 353 ms
- Candidates: 10
- Usable candidates: 8 (80.0%)
- Writer-ready candidates: 8 (80.0%)
- Status counts: enriched: 5, failed: 2, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 5, none: 2
- Failure reasons: access_denied: 5
- Extracted tokens: p50 1651, p90 3173, max 3532

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 2 | 2 | 2 | 0 | 0 | 878 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2634 |
| openai-blog | 4 | 2 | 0 | 2 | 2 | 0 |
