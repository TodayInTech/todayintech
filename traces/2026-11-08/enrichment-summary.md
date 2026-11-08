# Enrichment Trace - 2026-11-08

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 499 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 3, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 3
- Failure reasons: access_denied: 5
- Extracted tokens: p50 1089, p90 1338, max 1400

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1089 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
