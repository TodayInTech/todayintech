# Enrichment Trace - 2026-11-25

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 186 ms
- Candidates: 12
- Usable candidates: 12 (100.0%)
- Writer-ready candidates: 11 (91.7%)
- Status counts: enriched: 11, fallback: 1
- Input strategies: chunk_selection: 1, feed_metadata_only: 1, full_content: 10
- Failure reasons: policy_rejected: 1
- Extracted tokens: p50 830, p90 1982, max 4778

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| github-blog | 1 | 1 | 1 | 0 | 0 | 775 |
| google-blog | 3 | 3 | 3 | 0 | 0 | 179 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1629 |
| openai-blog | 4 | 4 | 4 | 0 | 0 | 1357 |
