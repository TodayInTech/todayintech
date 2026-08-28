# Enrichment Trace - 2026-08-28

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 135 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 14 (100.0%)
- Status counts: enriched: 10, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 10
- Failure reasons: access_denied: 4
- Extracted tokens: p50 972, p90 1683, max 2675

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 832 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2675 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 506 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1184 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
