# Enrichment Trace - 2026-09-11

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 111 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 14 (100.0%)
- Status counts: enriched: 9, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 9
- Failure reasons: access_denied: 5
- Extracted tokens: p50 1000, p90 1671, max 2958

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 920 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2958 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 220 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1101 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
