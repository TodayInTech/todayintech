# Enrichment Trace - 2026-08-20

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 407 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 4, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 4
- Failure reasons: access_denied: 4
- Extracted tokens: p50 888, p90 1171, max 1250

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 1 | 1 | 1 | 0 | 0 | 788 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 987 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
