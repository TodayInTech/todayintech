# Enrichment Trace - 2026-10-20

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 38 ms
- Candidates: 6
- Usable candidates: 6 (100.0%)
- Writer-ready candidates: 6 (100.0%)
- Status counts: enriched: 5, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 5
- Failure reasons: access_denied: 1
- Extracted tokens: p50 1119, p90 1731, max 2079

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1119 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1037 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
