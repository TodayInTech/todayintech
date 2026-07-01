# Enrichment Trace - 2026-07-01

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 543 ms
- Candidates: 9
- Usable candidates: 8 (88.9%)
- Writer-ready candidates: 7 (77.8%)
- Status counts: enriched: 7, failed: 1, fallback: 1
- Input strategies: evidence_selection: 1, feed_metadata_only: 1, full_content: 6, none: 1
- Failure reasons: access_denied: 1, extraction_failed: 1
- Extracted tokens: p50 1752, p90 6092, max 9910

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 3547 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1236 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 1012 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 2482 |
| openai-blog | 1 | 0 | 0 | 0 | 1 | 0 |
