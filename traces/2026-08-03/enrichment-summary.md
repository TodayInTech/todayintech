# Enrichment Trace - 2026-08-03

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 732 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 7 (100.0%)
- Status counts: enriched: 5, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 5
- Failure reasons: access_denied: 1, extraction_failed: 1
- Extracted tokens: p50 1568, p90 2119, max 2233

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1568 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 411 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1947 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
