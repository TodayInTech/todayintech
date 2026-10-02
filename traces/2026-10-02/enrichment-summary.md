# Enrichment Trace - 2026-10-02

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 103 ms
- Candidates: 10
- Usable candidates: 10 (100.0%)
- Writer-ready candidates: 9 (90.0%)
- Status counts: enriched: 7, fallback: 3
- Input strategies: chunk_selection: 1, feed_metadata_only: 3, full_content: 6
- Failure reasons: access_denied: 3
- Extracted tokens: p50 1321, p90 4117, max 4802

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 1 | 1 | 1 | 0 | 0 | 966 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1321 |
| google-blog | 1 | 1 | 1 | 0 | 0 | 169 |
| hacker-news | 4 | 4 | 4 | 0 | 0 | 3348 |
| openai-blog | 3 | 3 | 0 | 3 | 0 | 0 |
