# Enrichment Trace - 2026-11-18

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 339 ms
- Candidates: 13
- Usable candidates: 13 (100.0%)
- Writer-ready candidates: 12 (92.3%)
- Status counts: enriched: 9, fallback: 4
- Input strategies: chunk_selection: 1, feed_metadata_only: 4, full_content: 8
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1861, p90 2750, max 4430

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1936 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 1226 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 2172 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
