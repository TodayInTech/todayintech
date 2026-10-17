# Enrichment Trace - 2026-10-17

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1345 ms
- Candidates: 5
- Usable candidates: 5 (100.0%)
- Writer-ready candidates: 5 (100.0%)
- Status counts: enriched: 2, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 2
- Failure reasons: access_denied: 2, thin_content: 1
- Extracted tokens: p50 957, p90 1078, max 1108

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 957 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
