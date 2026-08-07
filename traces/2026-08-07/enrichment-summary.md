# Enrichment Trace - 2026-08-07

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 62 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 6, fallback: 2
- Input strategies: feed_metadata_only: 2, full_content: 6
- Failure reasons: access_denied: 2
- Extracted tokens: p50 1117, p90 1772, max 2026

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1460 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 759 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1146 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
