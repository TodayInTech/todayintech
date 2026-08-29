# Enrichment Trace - 2026-08-29

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 38 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 8, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 8
- Failure reasons: access_denied: 1
- Extracted tokens: p50 1016, p90 2791, max 2819

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 1016 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1812 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
