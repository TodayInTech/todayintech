# Enrichment Trace - 2026-07-28

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 712 ms
- Candidates: 14
- Usable candidates: 14 (100.0%)
- Writer-ready candidates: 13 (92.9%)
- Status counts: enriched: 12, fallback: 2
- Input strategies: evidence_selection: 1, feed_metadata_only: 2, full_content: 11
- Failure reasons: access_denied: 1, thin_content: 1
- Extracted tokens: p50 1766, p90 3774, max 154546

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| anthropic-blog | 4 | 4 | 4 | 0 | 0 | 3136 |
| github-blog | 1 | 1 | 1 | 0 | 0 | 1825 |
| google-blog | 4 | 4 | 4 | 0 | 0 | 740 |
| hacker-news | 4 | 4 | 3 | 1 | 0 | 1708 |
| openai-blog | 1 | 1 | 0 | 1 | 0 | 0 |
