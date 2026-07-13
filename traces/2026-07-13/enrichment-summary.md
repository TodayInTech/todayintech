# Enrichment Trace - 2026-07-13

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 67 ms
- Candidates: 8
- Usable candidates: 7 (87.5%)
- Writer-ready candidates: 7 (87.5%)
- Status counts: enriched: 6, failed: 1, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 6, none: 1
- Failure reasons: access_denied: 2
- Extracted tokens: p50 850, p90 2439, max 3463

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 850 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 938 |
| openai-blog | 2 | 1 | 0 | 1 | 1 | 0 |
