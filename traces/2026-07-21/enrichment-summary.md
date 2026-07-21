# Enrichment Trace - 2026-07-21

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 136 ms
- Candidates: 7
- Usable candidates: 7 (100.0%)
- Writer-ready candidates: 7 (100.0%)
- Status counts: enriched: 3, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 3
- Failure reasons: access_denied: 4
- Extracted tokens: p50 888, p90 1223, max 1307

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1307 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 870 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
