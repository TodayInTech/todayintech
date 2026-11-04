# Enrichment Trace - 2026-11-04

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 261 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 10 (90.9%)
- Status counts: enriched: 7, fallback: 4
- Input strategies: evidence_selection: 1, feed_metadata_only: 4, full_content: 6
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1311, p90 4953, max 8264

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1512 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 602 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 2028 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
