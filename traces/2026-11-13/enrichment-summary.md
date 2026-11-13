# Enrichment Trace - 2026-11-13

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 234 ms
- Candidates: 15
- Usable candidates: 15 (100.0%)
- Writer-ready candidates: 14 (93.3%)
- Status counts: enriched: 11, fallback: 4
- Input strategies: evidence_selection: 1, feed_metadata_only: 4, full_content: 10
- Failure reasons: access_denied: 4
- Extracted tokens: p50 1300, p90 3601, max 8404

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 2138 |
| github-blog | 2 | 2 | 2 | 0 | 0 | 2711 |
| google-blog | 4 | 4 | 4 | 0 | 0 | 394 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 1596 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
