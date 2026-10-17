# Enrichment Trace - 2026-10-17

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 160 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 6 (85.7%)
- Status counts: enriched: 4, fallback: 3
- Input strategies: chunk_selection: 1, feed_metadata_only: 3, full_content: 3
- Failure reasons: access_denied: 3
- Extracted tokens: p50 2523, p90 4149, max 4692

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 2523 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
