# Enrichment Trace - 2026-10-03

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 261 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 8 (88.9%)
- Status counts: enriched: 6, fallback: 3
- Input strategies: evidence_selection: 1, feed_metadata_only: 3, full_content: 5
- Failure reasons: access_denied: 2, unsupported_content_type: 1
- Extracted tokens: p50 1706, p90 7990, max 14053

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1563 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 745 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1928 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1850 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
