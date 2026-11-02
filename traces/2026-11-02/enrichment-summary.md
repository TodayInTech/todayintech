# Enrichment Trace - 2026-11-02

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 437 ms
- Candidates: 8
- Usable candidates: 5 (62.5%)
- Writer-ready candidates: 4 (50.0%)
- Status counts: enriched: 4, failed: 3, fallback: 1
- Input strategies: chunk_selection: 1, feed_metadata_only: 1, full_content: 3, none: 3
- Failure reasons: access_denied: 3, thin_content: 1
- Extracted tokens: p50 2254, p90 4122, max 4723

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1789 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2718 |
| openai-blog | 3 | 0 | 0 | 0 | 3 | 0 |
