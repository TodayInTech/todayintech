# Enrichment Trace - 2026-11-14

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 5267 ms
- Candidates: 16
- Usable candidates: 16 (100.0%)
- Writer-ready candidates: 16 (100.0%)
- Status counts: enriched: 10, fallback: 6
- Input strategies: feed_metadata_only: 6, full_content: 10
- Failure reasons: access_denied: 4, thin_content: 1, title_mismatch: 1
- Extracted tokens: p50 1084, p90 2403, max 2547

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1778 |
| google-blog | 4 | 4 | 4 | 0 | 0 | 561 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 902 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
