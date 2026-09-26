# Enrichment Trace - 2026-09-26

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 86 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 9 (90.0%)
- Status counts: enriched: 7, fallback: 3
- Input strategies: evidence_selection: 1, feed_metadata_only: 3, full_content: 6
- Failure reasons: access_denied: 3
- Extracted tokens: p50 1423, p90 4858, max 8204

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1394 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1008 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 2025 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
