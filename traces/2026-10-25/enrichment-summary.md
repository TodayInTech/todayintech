# Enrichment Trace - 2026-10-25

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 114 ms
- Candidates: 8
- Usable candidates: 6 (75.0%)
- Writer-ready candidates: 6 (75.0%)
- Status counts: enriched: 3, failed: 2, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 3, none: 2
- Failure reasons: access_denied: 5
- Extracted tokens: p50 1563, p90 1626, max 1642

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1563 |
| openai-blog | 4 | 2 | 0 | 2 | 2 | 0 |
