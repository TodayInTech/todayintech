# Enrichment Trace - 2026-10-31

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 576 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 10 (100.0%)
- Status counts: enriched: 5, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 5
- Failure reasons: access_denied: 5
- Extracted tokens: p50 1682, p90 2652, max 2949

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 2 | 2 | 1 | 1 | 0 | 280 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1944 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
