# Enrichment Trace - 2026-08-08

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 48 ms
- Candidates: 5
- Usable candidates: 5 (100.0%)
- Writer-ready candidates: 5 (100.0%)
- Status counts: enriched: 3, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 3
- Failure reasons: access_denied: 2
- Extracted tokens: p50 1207, p90 1418, max 1471

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1207 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
