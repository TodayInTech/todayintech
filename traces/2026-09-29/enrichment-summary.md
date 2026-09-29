# Enrichment Trace - 2026-09-29

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 73 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 10 (100.0%)
- Status counts: enriched: 7, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 7
- Failure reasons: access_denied: 3
- Extracted tokens: p50 2610, p90 3067, max 3194

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 3088 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 198 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1649 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
