# Enrichment Trace - 2026-10-22

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 98 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 12 (100.0%)
- Status counts: enriched: 8, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 8
- Failure reasons: access_denied: 4
- Extracted tokens: p50 886, p90 2258, max 2835

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 2 | 2 | 2 | 0 | 0 | 1786 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2011 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 945 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 553 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
