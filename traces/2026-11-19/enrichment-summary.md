# Enrichment Trace - 2026-11-19

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 693 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 12 (100.0%)
- Status counts: enriched: 7, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 7
- Failure reasons: access_denied: 4, thin_content: 1
- Extracted tokens: p50 1267, p90 2537, max 3142

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 3142 |
| google-blog | 3 | 3 | 2 | 1 | 0 | 448 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1358 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
