# Enrichment Trace - 2026-07-31

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 498 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 10 (90.9%)
- Status counts: enriched: 6, fallback: 5
- Input strategies: chunk_selection: 1, feed_metadata_only: 5, full_content: 5
- Failure reasons: access_denied: 4, title_mismatch: 1
- Extracted tokens: p50 2074, p90 4980, max 6341

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 2154 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 6341 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1916 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
