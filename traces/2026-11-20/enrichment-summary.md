# Enrichment Trace - 2026-11-20

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 338 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 12 (85.7%)
- Status counts: enriched: 9, fallback: 5
- Input strategies: chunk_selection: 2, feed_metadata_only: 5, full_content: 7
- Failure reasons: access_denied: 4, extraction_failed: 1
- Extracted tokens: p50 445, p90 5947, max 7044

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 391 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1271 |
| google-blog | 4 | 4 | 4 | 0 | 0 | 171 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 5673 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
