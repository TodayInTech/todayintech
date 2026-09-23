# Enrichment Trace - 2026-09-22

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 340 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 2, fallback: 6
- Input strategies: feed_metadata_only: 6, full_content: 2
- Failure reasons: access_denied: 6
- Extracted tokens: p50 1320, p90 1321, max 1321

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1320 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
