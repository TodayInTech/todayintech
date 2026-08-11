# Enrichment Trace - 2026-08-11

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 119 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 10 (100.0%)
- Status counts: enriched: 5, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 5
- Failure reasons: access_denied: 5
- Extracted tokens: p50 657, p90 1007, max 1189

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 735 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 229 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 657 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
