# Enrichment Trace - 2026-08-29

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 79 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 9, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 9
- Failure reasons: access_denied: 2
- Extracted tokens: p50 2444, p90 3095, max 3446

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 2337 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1188 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 2726 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
