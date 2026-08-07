# Enrichment Trace - 2026-08-07

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 91 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 7, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 7
- Failure reasons: access_denied: 2
- Extracted tokens: p50 1139, p90 1621, max 1749

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1528 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 158 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1136 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
