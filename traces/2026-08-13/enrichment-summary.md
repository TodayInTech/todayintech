# Enrichment Trace - 2026-08-13

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 815 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 7, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 7
- Failure reasons: access_denied: 3, thin_content: 1
- Extracted tokens: p50 1004, p90 2007, max 2213

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1721 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 404 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1004 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
