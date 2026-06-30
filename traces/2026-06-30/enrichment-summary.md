# Enrichment Trace - 2026-06-30

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1677 ms
- Candidates: 11
- Usable candidates: 10 (90.9%)
- Writer-ready candidates: 10 (90.9%)
- Status counts: enriched: 5, failed: 1, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 5, none: 1
- Failure reasons: access_denied: 5, thin_content: 1
- Extracted tokens: p50 1567, p90 2048, max 2168

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1869 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1567 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 994 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1734 |
| openai-blog | 4 | 3 | 0 | 3 | 1 | 0 |
