# Enrichment Trace - 2026-10-30

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 609 ms
- Candidates: 9
- Usable candidates: 8 (88.9%)
- Writer-ready candidates: 8 (88.9%)
- Status counts: enriched: 3, failed: 1, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 3, none: 1
- Failure reasons: access_denied: 6
- Extracted tokens: p50 1069, p90 2027, max 2267

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 1 | 1 | 1 | 0 | 0 | 693 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1668 |
| openai-blog | 4 | 3 | 0 | 3 | 1 | 0 |
