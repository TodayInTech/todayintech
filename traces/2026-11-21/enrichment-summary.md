# Enrichment Trace - 2026-11-21

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 407 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 10 (90.9%)
- Status counts: enriched: 9, fallback: 2
- Input strategies: chunk_selection: 1, feed_metadata_only: 2, full_content: 8
- Failure reasons: access_denied: 1, thin_content: 1
- Extracted tokens: p50 1018, p90 3340, max 6719

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 748 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 500 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1727 |
| openai-blog | 4 | 4 | 3 | 1 | 0 | 1353 |
