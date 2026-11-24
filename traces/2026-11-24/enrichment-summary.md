# Enrichment Trace - 2026-11-24

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 991 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 10 (100.0%)
- Status counts: enriched: 8, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 8
- Failure reasons: thin_content: 2
- Extracted tokens: p50 586, p90 2550, max 3440

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 2 | 2 | 2 | 0 | 0 | 780 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 342 |
| openai-blog | 4 | 4 | 3 | 1 | 0 | 573 |
