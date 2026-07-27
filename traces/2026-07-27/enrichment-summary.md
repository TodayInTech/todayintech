# Enrichment Trace - 2026-07-27

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 61 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 7 (100.0%)
- Status counts: enriched: 5, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 5
- Failure reasons: access_denied: 2
- Extracted tokens: p50 1745, p90 3518, max 3690

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 2148 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1745 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
