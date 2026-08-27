# Enrichment Trace - 2026-08-27

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 90 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 11 (91.7%)
- Status counts: enriched: 8, fallback: 4
- Input strategies: chunk_selection: 1, feed_metadata_only: 4, full_content: 7
- Failure reasons: access_denied: 4
- Extracted tokens: p50 960, p90 4117, max 4802

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 960 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 708 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 3823 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
