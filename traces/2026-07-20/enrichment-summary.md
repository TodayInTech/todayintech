# Enrichment Trace - 2026-07-20

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 769 ms
- Candidates: 8
- Usable candidates: 7 (87.5%)
- Writer-ready candidates: 7 (87.5%)
- Status counts: enriched: 4, failed: 1, fallback: 3
- Input strategies: feed_metadata_only: 3, full_content: 4, none: 1
- Failure reasons: access_denied: 2, thin_content: 1, title_mismatch: 1
- Extracted tokens: p50 1662, p90 1896, max 1977

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 1977 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1706 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1514 |
| openai-blog | 2 | 1 | 0 | 1 | 1 | 0 |
