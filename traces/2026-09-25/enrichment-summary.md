# Enrichment Trace - 2026-09-25

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 204 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 9 (90.0%)
- Status counts: enriched: 5, fallback: 5
- Input strategies: evidence_selection: 1, feed_metadata_only: 5, full_content: 4
- Failure reasons: access_denied: 5
- Extracted tokens: p50 2667, p90 10463, max 14894

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 2 | 2 | 2 | 0 | 0 | 2038 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 3817 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
