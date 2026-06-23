# QUALITY

This document defines the development verification and operational tracing flow for Today in Tech.

## Concept Boundaries

- `test`: verifies code behavior with fixtures and contracts.
- `trace`: records real operational collector/preprocessor/enrichment/writer results and durations.
- `quality`: runs `test` and `trace` together to produce deployment decision evidence.

## Make Commands

```bash
make test
make test-unit
make test-collection
make trace-collect
make trace-preprocess
make trace-enrich
make trace-write
make fetch-trace-history
make quality
```

## Artifacts

```text
.var/local/reports/
└── junit.xml

.var/local/traces/YYYY-MM-DD/
├── collection.json
├── enrichment.json
├── enrichment-summary.md
├── preprocessing.json
├── preprocessing-summary.md
├── writer-decisions.json
├── writer-decisions-summary.md
└── summary.md
```

`.var/local/reports/` and `.var/local/traces/` are not committed to Git. GitHub Actions uploads them as artifacts.

GitHub Actions artifacts are separated from local artifacts under `.artifacts/`.

```text
.artifacts/
├── raw/
├── reports/
└── traces/
```

## Trace History

Operational traces are not committed to the `main` branch. After the collector trace run, GitHub Actions publishes only trace results to the dedicated `tracing-history` branch, accumulated by date.

```text
tracing-history
└── traces/
    └── YYYY-MM-DD/
        ├── collection.json
        ├── enrichment.json
        ├── enrichment-summary.md
        ├── preprocessing.json
        ├── preprocessing-summary.md
        └── summary.md
```

Rules:

- `main` contains only code, configuration, and human-maintained documents.
- `tracing-history` is the long-term branch for operational trace records.
- Raw collection data and test reports remain GitHub Actions artifacts only.
- Re-running the workflow for the same date refreshes that date's trace files and commits only when there are changes.

Use this command to fetch accumulated trace data locally.

```bash
make fetch-trace-history
```

The default checkout path is `.var/remote/tracing-history`.

## Current Metrics

- Collection stage status
- Total collection duration
- Service-level status
- Service-level collector strategy
- Service-level article count
- Service-level duration
- Average duration per article
- Warning codes
- Error message
- Preprocessing duration
- Preprocessing candidate count
- Preprocessing excluded count
- Preprocessing excluded reason count
- Enrichment usable count and usable rate overall and by service
- Enrichment status and Agent input strategy distributions
- Source HTTP status, MIME type, response size, and fetch/extraction/selection durations
- Extractor and policy versions plus cache usage
- Document type and detected language
- Extracted token distribution and selected token ratio
- Section, chunk, code block, table, and list item counts
- Title similarity and extraction quality score
- Enrichment failure reason count

Enrichment trace statuses have the following meanings:

- `enriched`: extracted source evidence is usable as Agent input.
- `fallback`: source evidence is unavailable, but feed metadata fallback is allowed.
- `skipped`: policy excluded the candidate from enrichment.
- `failed`: no evidence is available for Writer.

Failure reasons are normalized to `fetch_failed`, `fetch_timeout`, `access_denied`, `rate_limited`, `unsupported_content_type`, `empty_content`, `thin_content`, `title_mismatch`, `extraction_failed`, `selection_failed`, `policy_rejected`, and `unknown`. HTTP status and concrete error details are stored separately.

Enrichment traces do not store source text or chunk text. They store only `content_hash` plus size, structure, status, and strategy metrics to avoid source replication and unbounded trace-history growth.

## Runtime Logs

The current full pipeline prints the following three numbered stages.

```text
[1/3] Collector
[2/3] Preprocessor
[3/3] Writer
```

Enrichment currently runs independently through `make enrich` or `make trace-enrich`. After Writer integration, the full pipeline log will expand to Collector, Preprocessor, Enrichment, and Writer.

Inside Writer, Agent editing, Markdown writing, and `briefed_articles` state updates are logged in order. The OpenAI Agent logs candidate review order, publish/skip decisions, structured output parse failures, and retry attempts. Writer decision trace stores per-candidate decision status, publish/reject rationale, confidence score, summary scope, and evidence basis as JSON and Markdown.

Published article pages do not expose internal decision details. Users see only a cohesive two-to-three-paragraph Korean summary covering the subject, central content, and technical significance, plus the source link. Publish rationale and evidence remain available through the Writer decision trace.

## Operating Rules

- Fixture-based `make test` is for stable development verification.
- `make trace-collect` calls real external sources and is for operational tracing.
- `make trace-preprocess` records preprocessing candidates and exclusion reasons from the collector raw snapshot.
- `make trace-enrich` records source fetching, extraction, structure, and input strategy for limited candidates.
- `make trace-write` records Writer Agent publish, skip, and failure decisions with evidence for each candidate.
- Trace duration is not used as a strict pass/fail condition because external network conditions can affect it.
- A service with zero articles records an `empty_collection` warning.
- Partial service failures are recorded in the trace, but the collector CLI exits successfully when at least one service succeeds.
- The collector CLI exits with failure when every service collection fails.
- GitHub Actions installs dev dependencies and sets `PYTHON=python` so CI does not depend on the local `.venv` path.
- GitHub Actions must commit generated `docs/` files and `data/briefed_articles.json` back to `main`. That state file is the duplicate-filtering source for later runs.
- The Markdown generator must normalize HTML and MDX tokens from external RSS, Atom, and sitemap sources into safe text.
- If OpenAI structured output fails because of token limits or JSON parsing, the agent retries once with a larger output limit and skips only the candidate that still fails.
