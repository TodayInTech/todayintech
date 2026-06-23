# Enrichment Trace - 2026-06-23

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1378 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 9 (100.0%)
- Status counts: enriched: 5, fallback: 4
- Input strategies: feed_metadata_only: 4, full_content: 5
- Failure reasons: access_denied: 2, extraction_failed: 1, title_mismatch: 1
- Extracted tokens: p50 1169, p90 2615, max 2693

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 1522 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 1169 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 1750 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
