# Enrichment Trace - 2026-11-23

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 269 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 7 (77.8%)
- Status counts: enriched: 8, fallback: 1
- Input strategies: chunk_selection: 2, feed_metadata_only: 1, full_content: 6
- Failure reasons: thin_content: 1
- Extracted tokens: p50 1809, p90 6668, max 7470

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 3840 |
| openai-blog | 5 | 5 | 5 | 0 | 0 | 989 |
