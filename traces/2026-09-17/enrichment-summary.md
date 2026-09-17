# Enrichment Trace - 2026-09-17

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 533 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 8 (88.9%)
- Status counts: enriched: 6, fallback: 3
- Input strategies: evidence_selection: 1, feed_metadata_only: 3, full_content: 5
- Failure reasons: access_denied: 2, title_mismatch: 1
- Extracted tokens: p50 848, p90 10462, max 19115

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1808 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 19115 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 772 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 562 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
