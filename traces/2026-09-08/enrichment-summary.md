# Enrichment Trace - 2026-09-08

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1572 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 12 (100.0%)
- Status counts: enriched: 7, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 7
- Failure reasons: access_denied: 4, extraction_failed: 1
- Extracted tokens: p50 1770, p90 2071, max 2184

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1884 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 495 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
