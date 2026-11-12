# Enrichment Trace - 2026-11-12

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 994 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 12 (100.0%)
- Status counts: enriched: 5, fallback: 7
- Input strategies: feed_metadata_only: 7, full_content: 5
- Failure reasons: access_denied: 6, thin_content: 1
- Extracted tokens: p50 445, p90 640, max 649

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 4 | 4 | 4 | 0 | 0 | 404 |
| hacker-news | 4 | 4 | 1 | 3 | 0 | 445 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
