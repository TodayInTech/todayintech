# Enrichment Trace - 2026-07-09

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 160 ms
- Candidates: 15
- Usable candidates: 14 (93.3%)
- Writer-ready candidates: 14 (93.3%)
- Status counts: enriched: 9, failed: 1, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 9, none: 1
- Failure reasons: access_denied: 6
- Extracted tokens: p50 876, p90 2420, max 2609

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 850 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2342 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 346 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1914 |
| openai-blog | 4 | 3 | 0 | 3 | 1 | 0 |
