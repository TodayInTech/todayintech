# Enrichment Trace - 2026-09-05

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 322 ms
- Candidates: 5
- Usable candidates: 5 (100.0%)
- Writer-ready candidates: 5 (100.0%)
- Status counts: enriched: 4, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 4
- Failure reasons: extraction_failed: 1
- Extracted tokens: p50 1028, p90 1794, max 2111

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2111 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1002 |
