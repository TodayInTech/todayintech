# Enrichment Trace - 2026-11-11

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 296 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 13 (92.9%)
- Status counts: enriched: 10, fallback: 4
- Input strategies: evidence_selection: 1, feed_metadata_only: 4, full_content: 9
- Failure reasons: access_denied: 4
- Extracted tokens: p50 826, p90 2717, max 9408

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 395 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1336 |
| google-blog | 4 | 4 | 4 | 0 | 0 | 220 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1858 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
