# Enrichment Trace - 2026-10-14

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 36 ms
- Candidates: 9
- Usable candidates: 9 (100.0%)
- Writer-ready candidates: 7 (77.8%)
- Status counts: enriched: 8, fallback: 1
- Input strategies: chunk_selection: 1, evidence_selection: 1, feed_metadata_only: 1, full_content: 6
- Failure reasons: access_denied: 1
- Extracted tokens: p50 2630, p90 9731, max 22132

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 2164 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 1504 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 4001 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
