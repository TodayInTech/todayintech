# Enrichment Trace - 2026-07-15

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 119 ms
- Candidates: 9
- Usable candidates: 8 (88.9%)
- Writer-ready candidates: 7 (77.8%)
- Status counts: enriched: 4, failed: 1, fallback: 4
- Input strategies: chunk_selection: 1, feed_metadata_only: 4, full_content: 3, none: 1
- Failure reasons: access_denied: 5
- Extracted tokens: p50 2752, p90 4998, max 5847

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 2238 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2486 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 4432 |
| openai-blog | 3 | 2 | 0 | 2 | 1 | 0 |
