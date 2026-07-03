# Enrichment Trace - 2026-07-03

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 41 ms
- Candidates: 8
- Usable candidates: 7 (87.5%)
- Writer-ready candidates: 6 (75.0%)
- Status counts: enriched: 7, failed: 1
- Input strategies: chunk_selection: 1, full_content: 6, none: 1
- Failure reasons: access_denied: 1
- Extracted tokens: p50 3103, p90 4589, max 5941

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 3 | 3 | 3 | 0 | 0 | 2726 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 3154 |
| openai-blog | 1 | 0 | 0 | 0 | 1 | 0 |
