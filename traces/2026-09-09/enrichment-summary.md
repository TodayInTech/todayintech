# Enrichment Trace - 2026-09-09

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 213 ms
- Candidates: 15
- Usable candidates: 15 (100.0%)
- Writer-ready candidates: 13 (86.7%)
- Status counts: enriched: 11, fallback: 4
- Input strategies: chunk_selection: 2, feed_metadata_only: 4, full_content: 9
- Failure reasons: access_denied: 4
- Extracted tokens: p50 946, p90 5736, max 5749

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 901 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 650 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 3998 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
