# Enrichment Trace - 2026-10-24

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 22894 ms
- Candidates: 8
- Usable candidates: 6 (75.0%)
- Writer-ready candidates: 6 (75.0%)
- Status counts: enriched: 1, failed: 2, fallback: 5
- Input strategies: feed_metadata_only: 5, full_content: 1, none: 2
- Failure reasons: access_denied: 4, empty_content: 1, extraction_failed: 1, thin_content: 1
- Extracted tokens: p50 386, p90 386, max 386

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 1 | 3 | 0 | 386 |
| openai-blog | 4 | 2 | 0 | 2 | 2 | 0 |
