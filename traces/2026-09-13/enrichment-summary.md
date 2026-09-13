# Enrichment Trace - 2026-09-13

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1289 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 7, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 7
- Failure reasons: thin_content: 1
- Extracted tokens: p50 970, p90 2350, max 2373

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 856 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2335 |
