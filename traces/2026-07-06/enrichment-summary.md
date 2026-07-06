# Enrichment Trace - 2026-07-06

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 81 ms
- Candidates: 6
- Usable candidates: 5 (83.3%)
- Writer-ready candidates: 4 (66.7%)
- Status counts: enriched: 5, failed: 1
- Input strategies: chunk_selection: 1, full_content: 4, none: 1
- Failure reasons: access_denied: 1
- Extracted tokens: p50 3221, p90 5015, max 5980

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1310 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 3394 |
| openai-blog | 1 | 0 | 0 | 0 | 1 | 0 |
