# Enrichment Trace - 2026-11-01

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 372 ms
- Candidates: 8
- Usable candidates: 5 (62.5%)
- Writer-ready candidates: 4 (50.0%)
- Status counts: enriched: 4, failed: 3, fallback: 1
- Input strategies: chunk_selection: 1, feed_metadata_only: 1, full_content: 3, none: 3
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1867, p90 4681, max 5230

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1867 |
| openai-blog | 4 | 1 | 0 | 1 | 3 | 0 |
