# Enrichment Trace - 2026-09-17

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1362 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 10 (90.9%)
- Status counts: enriched: 6, fallback: 5
- Input strategies: evidence_selection: 1, feed_metadata_only: 5, full_content: 5
- Failure reasons: access_denied: 4, extraction_failed: 1
- Extracted tokens: p50 1210, p90 7592, max 13143

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 3 | 3 | 3 | 0 | 0 | 862 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2040 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
