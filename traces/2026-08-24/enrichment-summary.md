# Enrichment Trace - 2026-08-24

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 98 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 7 (100.0%)
- Status counts: enriched: 6, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 6
- Failure reasons: access_denied: 1
- Extracted tokens: p50 1239, p90 3066, max 3555

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2576 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1714 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 724 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
