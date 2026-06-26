# Enrichment Trace - 2026-06-26

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 30 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 7 (100.0%)
- Status counts: enriched: 6, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 6
- Failure reasons: access_denied: 1
- Extracted tokens: p50 1306, p90 2175, max 2648

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1702 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 578 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1306 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
