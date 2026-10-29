# Original evidence retrieval and recovery

## Retrieval flow

```text
Candidate URL
  → Resolve original downloads (GitHub PDF viewer → raw file)
  → HTTP fetch (20 MiB download limit)
  → Bounded retries for network failures, 5xx and 429
  → Retry official OpenAI /index trailing-slash URL on 403/404
  → HTML precision extraction → balanced retry if empty or below minimum
  → PDF text extraction into page evidence blocks
  → Existing title, minimum-token and evidence-selection checks
  → Writer
```

All immediate retries share the existing `enrichment_max_attempts` budget. A 401 is not retried. A numeric Retry-After of 0–5 seconds is honored; longer values and HTTP dates are not immediately retried. With no header, the delay is one second. Canonical-path retry uses the publisher's official endpoint, without proxies or challenge bypass. Remaining 403 responses stay `access_denied`.

Balanced extraction uses the same HTML response only when precision output is empty or below the configured minimum. Sufficient precision output stays unchanged. Existing title and token thresholds remain in force; challenge/login titles are rejected. Metrics record `extraction_method` as `precision`, `balanced_retry` or `pdf_text`. The changed extractor version invalidates old extraction cache keys.

PDF responses require a binary signature and use pypdf text extraction. Encrypted files, documents over 100 pages and page content streams over 10 MiB are rejected. There is no OCR or complete formula/table reconstruction. Existing Writer evidence budgets still apply. Original source URLs remain unchanged; actual downloads are recorded as `final_url`.

## Durable recovery queue

`data/evidence_requests.json` lives next to the briefed state file. This generated metadata contains no original body, binary PDF or evidence chunk text.

- `pending`: original evidence failed or only feed metadata was available; first recheck is due one day later.
- `ready`: original evidence recovered; already published URLs are not regenerated.
- `reviewed`: Writer published, drafted or explicitly rejected the recovered article.
- `exhausted`: seven queue rechecks failed; manual review is needed.

The complete pipeline enriches current candidates and checks up to five due recovery requests per execution. Current candidate URLs are excluded from duplicate same-run requests. Queue retries back off by 2, 4, 7, 7… days, independently of ordinary candidate processing. Queued articles remain eligible even after dropping out of the feed or being excluded by candidate limits. Ordinary limit-excluded candidates are not all queued automatically.

Recovered evidence is merged into Writer input only after checking active URLs, same-service title fingerprints and existing document files. Already published/draft articles receive evidence status updates only. Explicit Writer rejection is acknowledged; transient Agent failures can be reviewed in a later run. Existing public articles are never automatically overwritten.

Daily automation commits queue metadata alongside generated archive state. Full recovery evidence is stored only in `.artifacts/enriched/{date}/recovery/` artifacts; `traces/{date}/evidence-recovery.json` holds counts and operational metrics only. Recovery creates neither a second article nor a new canonical URL for an existing article.

Previous failures can be seeded and rechecked without generating articles:

```bash
.venv/bin/python -m src.enrichment.recovery \
  --seed .var/local/enriched/2026-10-27/enrichment.json \
  --retry-now
```

The command checks up to five requests and writes `.var/local/recovered/{date}/enrichment.json`. It does not call the Agent or modify public documents. The default queue is next to the briefed state; `--queue` supports isolation. `--retry-now` makes pending requests due immediately, without reviving exhausted requests.

## Live recheck on 2026-10-29

Four problematic articles from the 2026-10-27 operational artifact were checked using the improved default Enricher. Access can vary by time and environment.

| Article | Previous problem | Observed result |
| --- | --- | --- |
| Decisions API | 403 or 62 demo tokens | Official slash URL returned 200; balanced extraction recovered 1,116 tokens, `full_content` |
| Exponential Time Hypothesis paper | 45 session-notice tokens from GitHub HTML viewer | Raw PDF returned 200; 63,222 extracted tokens, then bounded `evidence_selection` |
| CodeRabbit security case | HTTP 403 | Still 403; feed fallback and pending recovery |
| What FDE means at OpenAI | HTTP 403; 49-character feed description insufficient for fallback | Still 403; failed and pending recovery |

Local reproduction output is `.var/local/evidence-recovery/probe/enrichment.json`. No existing article was regenerated and no LLM call was made. Local success does not prove success from GitHub Actions; remaining access denials must be monitored through the queue and recovery metrics.
