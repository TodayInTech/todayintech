# Enrichment Trace - 2026-09-07

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 527 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 5, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 5
- Failure reasons: access_denied: 2, title_mismatch: 1
- Extracted tokens: p50 353, p90 679, max 732

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 2 | 2 | 2 | 0 | 0 | 666 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 299 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
