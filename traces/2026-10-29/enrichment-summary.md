# Enrichment Trace - 2026-10-29

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 104 ms
- Candidates: 13
- Usable candidates: 11 (84.6%)
- Writer-ready candidates: 9 (69.2%)
- Status counts: enriched: 9, failed: 2, fallback: 2
- Input strategies: chunk_selection: 2, feed_metadata_only: 2, full_content: 7, none: 2
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1471, p90 4596, max 6470

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 1114 |
| github-blog | 2 | 2 | 2 | 0 | 0 | 3939 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 358 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 2366 |
| openai-blog | 4 | 2 | 0 | 2 | 2 | 0 |
