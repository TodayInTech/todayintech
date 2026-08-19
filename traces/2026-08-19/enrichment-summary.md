# Enrichment Trace - 2026-08-19

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 403 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 10 (100.0%)
- Status counts: enriched: 5, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 5
- Failure reasons: access_denied: 5
- Extracted tokens: p50 955, p90 1158, max 1234

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1234 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 955 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 917 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
