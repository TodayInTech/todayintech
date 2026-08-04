# Enrichment Trace - 2026-08-04

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 173 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 8, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 8
- Failure reasons: access_denied: 3
- Extracted tokens: p50 984, p90 1682, max 2043

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 702 |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1655 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1528 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 418 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
