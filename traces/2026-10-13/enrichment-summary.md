# Enrichment Trace - 2026-10-13

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 383 ms
- Candidates: 6
- Usable candidates: 6 (100.0%)
- Writer-ready candidates: 6 (100.0%)
- Status counts: enriched: 5, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 5
- Failure reasons: thin_content: 1
- Extracted tokens: p50 1206, p90 1398, max 1501

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1206 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1243 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 671 |
