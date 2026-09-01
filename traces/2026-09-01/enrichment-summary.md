# Enrichment Trace - 2026-09-01

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 113 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 7 (87.5%)
- Status counts: enriched: 5, fallback: 3
- Input strategies: chunk_selection: 1, feed_metadata_only: 3, full_content: 4
- Failure reasons: access_denied: 3
- Extracted tokens: p50 352, p90 3158, max 4288

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 4288 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 256 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 352 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
