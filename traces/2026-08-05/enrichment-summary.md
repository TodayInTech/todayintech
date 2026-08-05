# Enrichment Trace - 2026-08-05

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 40 ms
- Candidates: 5
- Usable candidates: 5 (100.0%)
- Writer-ready candidates: 5 (100.0%)
- Status counts: enriched: 4, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 4
- Failure reasons: access_denied: 1
- Extracted tokens: p50 1056, p90 1865, max 2060

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1056 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
