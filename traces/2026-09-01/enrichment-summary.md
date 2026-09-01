# Enrichment Trace - 2026-09-01

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 185 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 9 (81.8%)
- Status counts: enriched: 8, fallback: 3
- Input strategies: chunk_selection: 1, evidence_selection: 1, feed_metadata_only: 3, full_content: 6
- Failure reasons: access_denied: 3
- Extracted tokens: p50 1055, p90 7177, max 13591

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 2535 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 908 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 2374 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
