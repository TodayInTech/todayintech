# Enrichment Trace - 2026-09-18

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 712 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 8 (80.0%)
- Status counts: enriched: 7, fallback: 3
- Input strategies: evidence_selection: 2, feed_metadata_only: 3, full_content: 5
- Failure reasons: access_denied: 2, thin_content: 1
- Extracted tokens: p50 807, p90 68422, max 154361

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 684 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1495 |
| google-blog | 2 | 2 | 2 | 0 | 0 | 642 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 11129 |
| openai-blog | 2 | 2 | 0 | 2 | 0 | 0 |
