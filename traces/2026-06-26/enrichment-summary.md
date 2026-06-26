# Enrichment Trace - 2026-06-26

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 40561 ms
- Candidates: 6
- Usable candidates: 6 (100.0%)
- Writer-ready candidates: 6 (100.0%)
- Status counts: enriched: 2, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 2
- Failure reasons: access_denied: 2, fetch_timeout: 1, thin_content: 1
- Extracted tokens: p50 1268, p90 1675, max 1777

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 1 | 1 | 0 | 760 |
| hacker-news | 4 | 4 | 1 | 3 | 0 | 1777 |
