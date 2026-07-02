# Enrichment Trace - 2026-07-02

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 755 ms
- Candidates: 6
- Usable candidates: 5 (83.3%)
- Writer-ready candidates: 5 (83.3%)
- Status counts: enriched: 4, failed: 1, fallback: 1
- Input strategies: feed_metadata_only: 1, full_content: 4, none: 1
- Failure reasons: access_denied: 1, thin_content: 1
- Extracted tokens: p50 1202, p90 2342, max 2651

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2651 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 781 |
| openai-blog | 1 | 0 | 0 | 0 | 1 | 0 |
