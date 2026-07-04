# Enrichment Trace - 2026-07-04

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 22 ms
- Candidates: 5
- Usable candidates: 4 (80.0%)
- Writer-ready candidates: 4 (80.0%)
- Status counts: enriched: 4, failed: 1
- Input strategies: full_content: 4, none: 1
- Failure reasons: access_denied: 1
- Extracted tokens: p50 642, p90 1062, max 1108

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 642 |
| openai-blog | 1 | 0 | 0 | 0 | 1 | 0 |
