# Enrichment Trace - 2026-10-24

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 313 ms
- Candidates: 8
- Usable candidates: 6 (75.0%)
- Writer-ready candidates: 5 (62.5%)
- Status counts: enriched: 3, failed: 2, fallback: 3
- Input strategies: chunk_selection: 1, feed_metadata_only: 3, full_content: 2, none: 2
- Failure reasons: access_denied: 4, thin_content: 1
- Extracted tokens: p50 2925, p90 4287, max 4628

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2925 |
| openai-blog | 4 | 2 | 0 | 2 | 2 | 0 |
