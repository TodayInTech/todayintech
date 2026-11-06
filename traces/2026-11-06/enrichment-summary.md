# Enrichment Trace - 2026-11-06

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1877 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 10 (90.9%)
- Status counts: enriched: 5, fallback: 6
- Input strategies: chunk_selection: 1, feed_metadata_only: 6, full_content: 4
- Failure reasons: access_denied: 4, thin_content: 1, title_mismatch: 1
- Extracted tokens: p50 1941, p90 3469, max 4014

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 2610 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1260 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 2296 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
