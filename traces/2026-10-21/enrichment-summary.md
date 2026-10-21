# Enrichment Trace - 2026-10-21

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 928 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 11 (91.7%)
- Status counts: enriched: 8, fallback: 4
- Input strategies: chunk_selection: 1, feed_metadata_only: 4, full_content: 7
- Failure reasons: access_denied: 2, extraction_failed: 1, thin_content: 1
- Extracted tokens: p50 1953, p90 3356, max 4325

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1721 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 4325 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 862 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1953 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
