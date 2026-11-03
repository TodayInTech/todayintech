# Enrichment Trace - 2026-11-03

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 540 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 5, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 5
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1617, p90 1826, max 1844

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1531 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1708 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
