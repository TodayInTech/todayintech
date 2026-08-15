# Enrichment Trace - 2026-08-15

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 35 ms
- Candidates: 4
- Usable candidates: 4 (100.0%)
- Writer-ready candidates: 3 (75.0%)
- Status counts: enriched: 3, fallback: 1
- Input strategies: chunk_selection: 1, feed_metadata_only: 1, full_content: 2
- Failure reasons: access_denied: 1
- Extracted tokens: p50 3859, p90 7125, max 7942

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 3859 |
