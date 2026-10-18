# Enrichment Trace - 2026-10-18

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 410 ms
- Candidates: 5
- Usable candidates: 5 (100.0%)
- Writer-ready candidates: 5 (100.0%)
- Status counts: enriched: 3, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 3
- Failure reasons: access_denied: 1, title_mismatch: 1
- Extracted tokens: p50 678, p90 1460, max 1656

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 678 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1052 |
