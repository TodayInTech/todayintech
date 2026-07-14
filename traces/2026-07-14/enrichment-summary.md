# Enrichment Trace - 2026-07-14

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 206 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 12 (100.0%)
- Status counts: enriched: 8, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 8
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1511, p90 2805, max 3257

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 2318 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 1180 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1844 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
