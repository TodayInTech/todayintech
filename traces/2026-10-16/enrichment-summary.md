# Enrichment Trace - 2026-10-16

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1666 ms
- Candidates: 15
- Usable candidates: 15 (100.0%)
- Writer-ready candidates: 15 (100.0%)
- Status counts: enriched: 10, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 10
- Failure reasons: access_denied: 5
- Extracted tokens: p50 896, p90 1269, max 1966

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 986 |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1552 |
| google-blog | 4 | 4 | 4 | 0 | 0 | 241 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 920 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
