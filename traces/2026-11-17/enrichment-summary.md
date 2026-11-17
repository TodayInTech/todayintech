# Enrichment Trace - 2026-11-17

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 615 ms
- Candidates: 9
- Usable candidates: 8 (88.9%)
- Writer-ready candidates: 8 (88.9%)
- Status counts: enriched: 4, failed: 1, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 4, none: 1
- Failure reasons: access_denied: 4, title_mismatch: 1
- Extracted tokens: p50 639, p90 2161, max 2810

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 1 | 1 | 1 | 0 | 0 | 630 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 648 |
| openai-blog | 4 | 3 | 0 | 3 | 1 | 0 |
