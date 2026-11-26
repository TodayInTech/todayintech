# Enrichment Trace - 2026-11-26

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 680 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 11 (91.7%)
- Status counts: enriched: 10, fallback: 2
- Input strategies: chunk_selection: 1, feed_metadata_only: 2, full_content: 9
- Failure reasons: empty_content: 1, thin_content: 1
- Extracted tokens: p50 1224, p90 2966, max 5947

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 3 | 3 | 3 | 0 | 0 | 1312 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 781 |
| openai-blog | 5 | 5 | 5 | 0 | 0 | 1209 |
