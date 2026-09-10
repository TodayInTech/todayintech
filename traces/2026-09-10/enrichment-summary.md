# Enrichment Trace - 2026-09-10

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 138 ms
- Candidates: 16
- Usable candidates: 16 (100.0%)
- Writer-ready candidates: 15 (93.8%)
- Status counts: enriched: 11, fallback: 5
- Input strategies: chunk_selection: 1, feed_metadata_only: 5, full_content: 10
- Failure reasons: access_denied: 5
- Extracted tokens: p50 855, p90 3375, max 4525

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1237 |
| github-blog | 2 | 2 | 2 | 0 | 0 | 2010 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 357 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 855 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
