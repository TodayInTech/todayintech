# Enrichment Trace - 2026-10-01

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 462 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 5, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 5
- Failure reasons: access_denied: 3, title_mismatch: 1
- Extracted tokens: p50 747, p90 1979, max 2109

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 2 | 2 | 2 | 0 | 0 | 167 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1785 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
