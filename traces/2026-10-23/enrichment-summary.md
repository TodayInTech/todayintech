# Enrichment Trace - 2026-10-23

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1180 ms
- Candidates: 11
- Usable candidates: 9 (81.8%)
- Writer-ready candidates: 9 (81.8%)
- Status counts: enriched: 6, failed: 2, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 6, none: 2
- Failure reasons: access_denied: 4, extraction_failed: 1
- Extracted tokens: p50 1042, p90 2973, max 3286

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 482 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2660 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1104 |
| openai-blog | 4 | 2 | 0 | 2 | 2 | 0 |
