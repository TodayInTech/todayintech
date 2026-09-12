# Enrichment Trace - 2026-09-12

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 139 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 10 (90.9%)
- Status counts: enriched: 7, fallback: 4
- Input strategies: chunk_selection: 1, feed_metadata_only: 4, full_content: 6
- Failure reasons: access_denied: 4
- Extracted tokens: p50 843, p90 2510, max 4533

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 792 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1161 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
