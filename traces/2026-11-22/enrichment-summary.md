# Enrichment Trace - 2026-11-22

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 554 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 7 (87.5%)
- Status counts: enriched: 6, fallback: 2
- Input strategies: chunk_selection: 1, feed_metadata_only: 2, full_content: 5
- Failure reasons: access_denied: 1, thin_content: 1
- Extracted tokens: p50 1470, p90 5125, max 7932

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2318 |
| openai-blog | 4 | 4 | 3 | 1 | 0 | 1265 |
