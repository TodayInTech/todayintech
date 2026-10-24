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
make build-operations
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

The Operations dashboard does not use local traces as input. `make build-operations` reads only the remote `tracing-history` checkout specified by `TRACE_HISTORY_DIR`, excludes source body text, selected chunk text, and detailed Agent rationale, then writes aggregate metrics to `static/data/operations/trace-metrics.json`. GitHub Actions pushes trace history, fetches the updated `tracing-history` branch again, builds Operations data, and then builds Docusaurus.

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
- Writer-ready count and rate for immediately consumable evidence
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

Collection trace statuses have the following meanings:

- `success`: no service failed or partially failed.
- `partial`: at least one service failed, or at least one service recorded recoverable warnings such as individual article metadata request failures.
- `failed`: every service collection failed.

## Runtime Logs

The full pipeline prints the following four numbered stages.

```text
[1/4] Collector
[2/4] Preprocessor
[3/4] Enrichment
[4/4] Writer
```

Enrichment can also run independently through `make enrich` or `make trace-enrich`.

Inside Writer, Agent editing, Markdown writing, and `briefed_articles` state updates are logged in order. The OpenAI Agent logs candidate review order, publish/skip decisions, structured output parse failures, and retry attempts. Writer decision trace stores per-candidate decision status, publish/reject rationale, confidence score, summary scope, and evidence basis as JSON and Markdown.

Public articles separate a one-to-two-sentence list summary (`summary_ko`) from a dynamic detailed body (`article_markdown_ko`). Headings, paragraphs, lists, tables and source-backed code/quotes are optional and article-specific. Ordinary news targets 800–1500 Korean characters and rich technical announcements 1500–2500+, with shorter output for sparse evidence. The generator adds the source link; rationale, confidence and evidence lists stay in traces.

## Operating Rules

- Fixture-based `make test` is for stable development verification.
- `make trace-collect` calls real external sources and is for operational tracing.
- `make trace-preprocess` records preprocessing candidates and exclusion reasons from the collector raw snapshot.
- `make trace-enrich` records source fetching, extraction, structure, and input strategy for limited candidates.
- `make trace-write` records Writer Agent publish, skip, and failure decisions with evidence for each candidate.
- Trace duration is not used as a strict pass/fail condition because external network conditions can affect it.
- A service with zero articles records an `empty_collection` warning.
- Sitemap collection skips only the affected URL and records an `article_metadata_fetch_failed` warning when an individual page metadata request fails.
- Partial service failures are recorded in the trace, but the collector CLI exits successfully when at least one service succeeds.
- The collector CLI exits with failure when every service collection fails.
- GitHub Actions installs dev dependencies and sets `PYTHON=python` so CI does not depend on the local `.venv` path.
- GitHub Actions must commit generated `docs/` files and `data/briefed_articles.json` back to `main`. That state file is the duplicate-filtering source for later runs.
- The Markdown generator must normalize HTML and MDX tokens from external RSS, Atom, and sitemap sources into safe text.
- If OpenAI structured output fails because of token limits or JSON parsing, the agent retries once with a larger output limit and skips only the candidate that still fails.

## UI verification (2026-10-16)

- Refined navigation, briefing cards, and traces using B4React's neutral surfaces, borders, and rounded controls as a reference.
- The dashboard still uses remote trace input. Service filters also scope trend charts. Metric names, statuses, and empty states use concise Korean/English copy; metric tooltips explain coverage and publication rates.
- Tooltips support keyboard focus/taps, Escape, and outside taps. Service selection uses a custom combobox/listbox with arrow-key, Enter, and Escape navigation. Animations respect reduced motion.
- Validation: six existing document-generation, article Markdown, and operations metric tests passed, along with Python lint/format and SVG XML validation. Both Docusaurus locales built successfully. Browser checks covered light/dark themes, 390px card/trace layouts, tooltip open/Escape dismissal, and service-scoped trend updates.

- Follow-up UI refinement restores original brand colors, removes icon frames and navigation/sidebar dividers, centers content, and applies 36px controls (44px on touch devices) with tighter card padding.

- Navigation regression checks: the sidebar remains 200px regardless of content. Dark-theme tokens and current-page backgrounds have higher specificity than shared defaults. Filters/pagination persist in the URL; the single article return link restores the originating list, falling back to the service list on direct entry. Empty states use the full list width and a 144px minimum height. Browser checks covered Anthropic page 2 → article → list and selected-page contrast in both themes.

- Shared DateCard covers the main update, briefing cards, article metadata, and trace update/run/table dates. Existing Markdown dates and feed extraction formats remain intact; MDX decorates metadata at render time. Cards align brand icons/names and remove footer copy. Trace service selection uses a custom combobox/listbox. Tooltips use black backgrounds in light mode and white backgrounds in dark mode. Browser checks covered keyboard selection, tooltip colors in both themes, and article dates. Six existing generation/operations tests and Python lint/format checks passed.

- Operations tables align dates, services, and statuses left, and numeric values/rates right. Headers and cells share alignment, vertical centering, and thin row separators. All services uses text without an icon.

- Dates use a small background treatment without icons or borders. Articles have one return link at the top. Table statuses use text color/weight without pill backgrounds.

- Main service filters only affect the mode=all list. Featured/new sections retain their fixed service scope. Filter/pagination updates preserve the current results footprint to prevent document-height shrinkage from clamping the scroll position; resizing resets the reserved height. Active navbar items use text color/weight without backgrounds or borders.

- Briefing cards use a fixed 16rem height, reserving two title lines and three excerpt lines. Browser checks on port 3100 confirmed unchanged featured/new article links after lower-list filtering and stable scroll position during keyboard period changes.

- Final verification: make check passed Ruff lint/format and all 67 tests; Korean/English static builds passed. Pagination retains first/last and immediate neighboring pages, with 1 … 25 26 27 … 30 verified at page 26 of 30. Browser measurements confirmed 256px cards and 48px title areas.

- Sidebar hover regression: reproduce and fix Infima's category-link `background: none !important` conflict. Verify Korean/English builds, light/dark hover on all six service navigation items, the selected service, keyboard focus, and hover on all six trace navigation items in the browser.

- Dynamic articles: `make check` passed Ruff lint/format and all 70 tests. Live old/new prompt generation on three identical cached source packets compared length, headings, numerical claims and evidence IDs. Korean/English Docusaurus builds and browser checks verified the 780px article reader, dynamic headings, source link, Markdown tables/lists/quotes/code and inert HTML/MDX/unsafe links. See [article generation verification](ARTICLE_GENERATION.md) for results and sampling limits.

- Article alignment/TOC: Korean/English builds and browser checks verified left-aligned H1–H6 rules, a sticky 200px right-side TOC, section navigation and active-item highlighting. At 390px the collapsible TOC remains available without horizontal overflow. Main title and section alignment remain unchanged.

- Emphasis: use short `**bold phrases**` selectively for core changes, decisive numbers and material limits. Avoid whole-paragraph, every-number or repeated emphasis, and verify bold syntax survives Markdown safety handling.
