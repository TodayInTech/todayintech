# Enrichment Trace - 2026-07-10

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 250 ms
- Candidates: 9
- Usable candidates: 7 (77.8%)
- Writer-ready candidates: 7 (77.8%)
- Status counts: enriched: 5, failed: 2, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 5, none: 2
- Failure reasons: access_denied: 3, unsupported_content_type: 1
- Extracted tokens: p50 1385, p90 2282, max 2348

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1318 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2348 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1385 |
| openai-blog | 3 | 1 | 0 | 1 | 2 | 0 |
