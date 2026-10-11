# Enrichment Trace - 2026-10-11

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 405 ms
- Candidates: 4
- Usable candidates: 4 (100.0%)
- Writer-ready candidates: 3 (75.0%)
- Status counts: enriched: 2, fallback: 2
- Input strategies: chunk_selection: 1, feed_metadata_only: 2, full_content: 1
- Failure reasons: access_denied: 1, title_mismatch: 1
- Extracted tokens: p50 3547, p90 5381, max 5839

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 3547 |
