# Enrichment Trace - 2026-06-23

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 3947 ms
- Candidates: 6
- Usable candidates: 6 (100.0%)
- Writer-ready candidates: 6 (100.0%)
- Status counts: enriched: 4, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 4
- Failure reasons: access_denied: 1, title_mismatch: 1
- Extracted tokens: p50 1764, p90 3056, max 3067

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 1 | 1 | 1 | 0 | 0 | 370 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 3029 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
