# Enrichment Trace - 2026-09-24

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 136 ms
- Candidates: 13
- Usable candidates: 13 (100.0%)
- Writer-ready candidates: 13 (100.0%)
- Status counts: enriched: 8, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 8
- Failure reasons: access_denied: 5
- Extracted tokens: p50 1104, p90 2435, max 3753

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 2626 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 635 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1325 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
