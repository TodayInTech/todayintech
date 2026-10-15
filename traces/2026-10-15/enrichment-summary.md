# Enrichment Trace - 2026-10-15

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 321 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 14 (100.0%)
- Status counts: enriched: 10, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 10
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1099, p90 1881, max 1979

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 1582 |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1604 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 158 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 903 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
