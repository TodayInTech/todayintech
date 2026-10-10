# Enrichment Trace - 2026-10-10

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 551 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 3, fallback: 6
- Input strategies: feed_metadata_only: 6, full_content: 3
- Failure reasons: access_denied: 5, extraction_failed: 1
- Extracted tokens: p50 1305, p90 1803, max 1928

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1305 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1170 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
