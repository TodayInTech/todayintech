# Enrichment Trace - 2026-07-24

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 153 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 7 (100.0%)
- Status counts: enriched: 4, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 4
- Failure reasons: access_denied: 3
- Extracted tokens: p50 899, p90 1408, max 1599

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 899 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
