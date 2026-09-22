# Enrichment Trace - 2026-09-22

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1174 ms
- Candidates: 8
- Usable candidates: 8 (100.0%)
- Writer-ready candidates: 8 (100.0%)
- Status counts: enriched: 1, fallback: 7
- Input strategies: feed_metadata_only: 7, full_content: 1
- Failure reasons: access_denied: 6, extraction_failed: 1
- Extracted tokens: p50 721, p90 721, max 721

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hacker-news | 4 | 4 | 1 | 3 | 0 | 721 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
