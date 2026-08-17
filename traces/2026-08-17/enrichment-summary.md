# Enrichment Trace - 2026-08-17

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 158 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 6, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 6
- Failure reasons: access_denied: 3
- Extracted tokens: p50 799, p90 1385, max 1506

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1264 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 523 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 799 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
