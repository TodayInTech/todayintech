# Enrichment Trace - 2026-08-01

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 57 ms
- Candidates: 6
- Usable candidates: 6 (100.0%)
- Writer-ready candidates: 6 (100.0%)
- Status counts: enriched: 4, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 4
- Failure reasons: access_denied: 2
- Extracted tokens: p50 1093, p90 1744, max 1999

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1093 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
