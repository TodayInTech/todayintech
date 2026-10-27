# Enrichment Trace - 2026-10-27

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 609 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 4, fallback: 7
- Input strategies: feed_metadata_only: 7, full_content: 4
- Failure reasons: access_denied: 6, thin_content: 1
- Extracted tokens: p50 583, p90 2444, max 3183

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 309 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 583 |
| hacker-news | 4 | 4 | 1 | 3 | 0 | 3183 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
