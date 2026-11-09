# Enrichment Trace - 2026-11-09

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 132 ms
- Candidates: 5
- Usable candidates: 5 (100.0%)
- Writer-ready candidates: 5 (100.0%)
- Status counts: enriched: 3, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 3
- Failure reasons: access_denied: 2
- Extracted tokens: p50 1323, p90 1397, max 1416

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1323 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
