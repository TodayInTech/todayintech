# Enrichment Trace - 2026-07-18

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 249 ms
- Candidates: 5
- Usable candidates: 4 (80.0%)
- Writer-ready candidates: 4 (80.0%)
- Status counts: enriched: 1, failed: 1, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 1, none: 1
- Failure reasons: access_denied: 4
- Extracted tokens: p50 649, p90 649, max 649

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 1 | 3 | 0 | 649 |
| openai-blog | 1 | 0 | 0 | 0 | 1 | 0 |
