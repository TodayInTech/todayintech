# Enrichment Trace - 2026-09-30

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 330 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 8 (88.9%)
- Status counts: enriched: 5, fallback: 4
- Input strategies: chunk_selection: 1, feed_metadata_only: 4, full_content: 4
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1408, p90 3770, max 4237

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1408 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1770 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
