# Enrichment Trace - 2026-10-07

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 367 ms
- Candidates: 13
- Usable candidates: 13 (100.0%)
- Writer-ready candidates: 13 (100.0%)
- Status counts: enriched: 8, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 8
- Failure reasons: access_denied: 4, fetch_failed: 1
- Extracted tokens: p50 1111, p90 1987, max 2154

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1818 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2154 |
| google-blog | 4 | 4 | 4 | 0 | 0 | 964 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1180 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
