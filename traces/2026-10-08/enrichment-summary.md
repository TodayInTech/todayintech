# Enrichment Trace - 2026-10-08

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 52 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 5, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 5
- Failure reasons: access_denied: 3
- Extracted tokens: p50 638, p90 1685, max 1688

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1688 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 239 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 638 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
