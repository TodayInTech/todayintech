# Enrichment Trace - 2026-08-18

## Summary

- Status: `partial`
- Policy: `adaptive-token-budget@1:min=100:full=4000:select=8000`
- Duration: 1340 ms
- Candidates: 11
- Usable candidates: 11 (100.0%)
- Writer-ready candidates: 11 (100.0%)
- Status counts: enriched: 5, fallback: 6
- Input strategies: feed_metadata_only: 6, full_content: 5
- Failure reasons: access_denied: 5, thin_content: 1
- Extracted tokens: p50 798, p90 1101, max 1151

## Services

| Service | Candidates | Usable | Enriched | Fallback | Failed | Tokens p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| google-blog | 3 | 3 | 3 | 0 | 0 | 798 |
| hacker-news | 4 | 4 | 2 | 2 | 0 | 883 |
| openai-blog | 4 | 4 | 0 | 4 | 0 | 0 |
