# Enrichment Trace - 2026-07-23

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 170 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 14 (100.0%)
- Status counts: enriched: 10, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 10
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1082, p90 1419, max 2181

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 3 | 3 | 3 | 0 | 0 | 1085 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 843 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 876 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
