# Enrichment Trace - 2026-11-16

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 300 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 5, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 5
- Failure reasons: access_denied: 3
- Extracted tokens: p50 417, p90 1343, max 1519

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 1298 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 368 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
