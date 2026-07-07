# Enrichment Trace - 2026-07-07

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 142 ms
- Candidates: 12
- Usable candidates: 11 (91.7%)
- Writer-ready candidates: 11 (91.7%)
- Status counts: enriched: 8, failed: 1, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 8, none: 1
- Failure reasons: access_denied: 4
- Extracted tokens: p50 654, p90 1408, max 1803

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1803 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 784 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 545 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 421 |
| openai-blog | 3 | 2 | 0 | 2 | 1 | 0 |
