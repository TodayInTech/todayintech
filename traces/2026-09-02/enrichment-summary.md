# Enrichment Trace - 2026-09-02

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1441 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 12 (100.0%)
- Status counts: enriched: 7, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 7
- Failure reasons: access_denied: 4, extraction_failed: 1
- Extracted tokens: p50 1281, p90 2371, max 2900

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1650 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 299 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 2101 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
