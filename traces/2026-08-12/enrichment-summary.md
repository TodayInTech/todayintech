# Enrichment Trace - 2026-08-12

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 138 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 7, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 7
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1281, p90 2967, max 3673

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 3 | 3 | 3 | 0 | 0 | 2496 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1236 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
