# Enrichment Trace - 2026-06-29

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 25 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 6 (75.0%)
- Status counts: enriched: 7, fallback: 1
- Input strategies: chunk_selection: 2, feed_metadata_only: 1, full_content: 5
- Failure reasons: access_denied: 1
- Extracted tokens: p50 2080, p90 4474, max 4943

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 3868 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1245 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1425 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
