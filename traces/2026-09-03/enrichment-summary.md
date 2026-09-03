# Enrichment Trace - 2026-09-03

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 174 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 6, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 6
- Failure reasons: access_denied: 5
- Extracted tokens: p50 868, p90 2756, max 3899

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 559 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 1232 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 884 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
