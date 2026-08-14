# Enrichment Trace - 2026-08-14

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 2496 ms
- Candidates: 6
- Usable candidates: 6 (100.0%)
- Writer-ready candidates: 4 (66.7%)
- Status counts: enriched: 5, fallback: 1
- Input strategies: chunk_selection: 1, evidence_selection: 1, feed_metadata_only: 1, full_content: 3
- Failure reasons: thin_content: 1
- Extracted tokens: p50 2630, p90 8501, max 9123

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 2630 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1206 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 7567 |
