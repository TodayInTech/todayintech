# Enrichment Trace - 2026-06-29

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 26 ms
- Candidates: 5
- Usable candidates: 5 (100.0%)
- Writer-ready candidates: 5 (100.0%)
- Status counts: enriched: 4, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 4
- Failure reasons: access_denied: 1
- Extracted tokens: p50 1462, p90 2511, max 2878

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1462 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
