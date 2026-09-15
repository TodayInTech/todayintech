# Enrichment Trace - 2026-09-15

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 845 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 7 (100.0%)
- Status counts: enriched: 4, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 4
- Failure reasons: access_denied: 2, extraction_failed: 1
- Extracted tokens: p50 1125, p90 2420, max 2673

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 2 | 2 | 2 | 0 | 0 | 300 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 2252 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
