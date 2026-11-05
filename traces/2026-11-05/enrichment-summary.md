# Enrichment Trace - 2026-11-05

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 672 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 7 (77.8%)
- Status counts: enriched: 4, fallback: 5
- Input strategies: chunk_selection: 2, feed_metadata_only: 5, full_content: 2
- Failure reasons: access_denied: 4, title_mismatch: 1
- Extracted tokens: p50 2419, p90 4997, max 5371

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 1 | 1 | 1 | 0 | 0 | 215 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 4124 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
