# ARCHITECTURE

## Project Architecture

Today in Tech separates collection, preprocessing, Writer, build, and deployment. Each stage should be independently testable, and adding a service must not require changing the whole pipeline.

```text
Official Sources
    ↓
Service Factory
    ↓
Service-specific Collector Strategy
    ↓
Normalize Articles
    ↓
Raw Snapshot Storage
    ↓
Preprocess Candidates
    ↓
Briefed Article Filtering
    ↓
Candidate Ranking
    ↓
Candidate Enrichment
    ↓
Writer
    ├── News Editor Agent
    └── Markdown Generator
    ↓
Docusaurus Build
    ↓
GitHub Pages Deployment
```

## Main Directories

```text
src/
├── sources/
│   ├── contracts/
│   │   └── base.py
│   ├── factory.py
│   └── implementations/
│       ├── hacker_news.py
│       ├── github_blog.py
│       ├── google_blog.py
│       ├── openai_blog.py
│       └── anthropic_blog.py
├── collection/
│   ├── __main__.py
│   ├── news_collector.py
│   ├── raw_writer.py
│   ├── factories/
│   │   └── collector_strategy_factory.py
│   └── strategies/
│       ├── base.py
│       ├── rss.py
│       └── sitemap.py
├── processing/
│   ├── __main__.py
│   ├── context.py
│   ├── enums.py
│   ├── models.py
│   ├── news_preprocessor.py
│   ├── processed_writer.py
│   ├── contracts/
│   │   └── base.py
│   ├── factories/
│   │   └── preprocessing_pipeline_factory.py
│   ├── identity/
│   │   ├── candidate_identity.py
│   │   └── url_normalizer.py
│   ├── policies/
│   │   ├── base.py
│   │   └── service_policy.py
│   ├── scoring/
│   │   ├── base.py
│   │   └── default.py
│   ├── state/
│   │   └── briefed_article_store.py
│   ├── steps/
│   │   ├── validation.py
│   │   ├── url_normalization.py
│   │   ├── candidate_identity.py
│   │   ├── run_deduplication.py
│   │   ├── briefed_article_filter.py
│   │   ├── candidate_scoring.py
│   │   ├── candidate_quality_gate.py
│   │   └── candidate_limiting.py
├── enrichment/
│   ├── __main__.py
│   ├── content_enricher.py
│   ├── context.py
│   ├── models.py
│   ├── contracts/
│   ├── factories/
│   ├── fetchers/
│   ├── extractors/
│   ├── chunking/
│   ├── policies/
│   ├── steps/
│   ├── state/
│   ├── storage/
│   └── tokenization/
├── writer/
│   ├── __main__.py
│   ├── news_writer.py
│   ├── agent/
│   │   ├── contracts.py
│   │   ├── draft_agent.py
│   │   └── schemas.py
│   └── generator/
│       ├── article_markdown_writer.py
│       ├── main_index_writer.py
│       └── service_index_writer.py
├── models/
│   └── article.py
└── main.py
```

## Service Extension Structure

Service creation follows Factory Method and Abstract Factory patterns. Collection algorithms are separated through the Strategy pattern.

- Product and documentation language uses `service` for the briefing unit exposed to users.
- Code uses `source` for external collection targets and `collection` for the execution layer.
- `BaseNewsSource`: service metadata and collector configuration interface
- `BaseCollectorStrategy`: collection algorithm interface
- `RssCollector`: RSS/Atom collection strategy
- `SitemapCollector`: sitemap + page metadata collection strategy
- `CollectorStrategyFactory`: creates collector strategies by `collector_type`
- `NewsSourceFactory`: creates concrete services by service key
- `AbstractNewsSourceFactory`: abstract factory for future service family expansion

When adding a new service, do not modify the existing pipeline. Add service metadata under `src/sources/implementations/` and register it in the factory registry.
Services without RSS must not rely on third-party RSS feeds. Choose or add an appropriate collector strategy such as official sitemap, official API, or HTML metadata collection.

## Generated Document Structure

The site is a cumulative archive, not a dated daily briefing bundle.

```text
docs/
├── index.md
├── services/
│   ├── hacker-news.md
│   ├── hacker-news/
│   ├── github-blog.md
│   ├── github-blog/
│   ├── google-blog.md
│   ├── google-blog/
│   ├── openai-blog.md
│   ├── openai-blog/
│   ├── anthropic-blog.md
│   └── anthropic-blog/
```

`index.md` is the entry point for cross-service highlights. `services/*.md` files are service-level indexes. `services/{service_key}/*.md` files are detailed briefings for individual source articles.
Individual article pages should favor a natural editorial briefing format over a rigid report format.

## Step-by-Step Flow

```text
Collector
    ↓
Preprocessor
    ↓
Writer
    ├── Agent
    └── Generator
    ↓
Build
    ↓
Deploy
```

## Collector

The Collector stage must be independently executable and make service-level collection results easy to inspect. The Collector is a daily snapshot discovery layer. Repeated articles across dates are expected; preprocessing is responsible for preventing reprocessing.

1. `NewsCollector` creates MVP service implementations through `NewsSourceFactory`.
2. Each service implementation collects information through its own collector strategy, such as RSS/Atom, sitemap, or official API.
3. Feed entries are normalized into the shared `Article` model.
4. Service-level collection results are wrapped as `ServiceCollectionResult`.
5. URL, title, publication date, source, summary, and tags are preserved where possible.
6. Collection results are stored as JSON under `.var/local/raw/{YYYY-MM-DD}/`.
7. Per-source collection scope may be limited through source configuration. Large feeds such as OpenAI should add `collection_limit` or `lookback_days`.

Collect every service:

```bash
make collect
```

Collect a single service:

```bash
make collect SERVICE=hacker-news COUNT=5
```

Collect for a specific date:

```bash
make collect SERVICE=hacker-news DATE=2026-06-07 COUNT=5
```

Available service keys are exposed through `NewsSourceFactory.service_keys()`. The collector CLI prints a console summary and writes the same results to `.var/local/raw/{YYYY-MM-DD}/summary.json` and `.var/local/raw/{YYYY-MM-DD}/services/{service}.json`. This stage does not generate Markdown or build Docusaurus.

MVP services:

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

Raw collection output:

```text
.var/local/raw/YYYY-MM-DD/
├── summary.json
└── services/
    ├── hacker-news.json
    ├── github-blog.json
    ├── google-blog.json
    ├── openai-blog.json
    └── anthropic-blog.json
```

## Preprocessor

The Preprocessor stage turns collected snapshots into agent-ready candidates.

1. Normalize URLs into canonical form.
2. Remove entries missing required fields.
3. Remove run-level duplicates by URL and title fingerprint.
4. Exclude already briefed articles through the `briefed_articles` state and existing article documents.
5. Rank candidates by publication date, source priority, popularity signals, and editorial keywords.
6. Limit the number of candidates passed to the agent.
7. Generate Writer-facing `candidate_id`, `url_hash`, `suggested_doc_key`, and `suggested_article_path`.
8. Generate preprocessing trace output.

The current scaffold is heuristic-based. The LLM-based News Editor Agent must receive only new preprocessed candidates.
The full `src.main` pipeline runs the Preprocessor immediately after the Collector and writes the preprocessing result to `.var/local/processed/{YYYY-MM-DD}/preprocessing.json`.

Preprocessing execution:

```bash
make preprocess
make preprocess DATE=2026-06-07
make preprocess RAW_DIR=.var/local/raw PROCESSED_DIR=.var/local/processed
```

Preprocessing output:

```text
.var/local/processed/YYYY-MM-DD/
└── preprocessing.json
```

Preprocessing uses a `Pipeline + Strategy + Repository` combination. `PreprocessingPipelineFactory` assembles the default step list, and `NewsPreprocessor` runs ordered `BasePreprocessingStep` objects. Step implementations under `processing/steps/` explicitly inherit from that ABC. Candidate scoring is kept as a `BaseCandidateScorer`-based strategy under `processing/scoring/`, while URL and document identity generation lives under `processing/identity/`. Service-level quality thresholds are defined through `ServicePreprocessingPolicy` under `processing/policies/`, and `CandidateQualityGateStep` filters low-quality candidates after scoring and before limiting. `BriefedArticleStore` lives under `processing/state/` and acts as the state repository for source articles recorded by Writer after successful document generation. Exclusion reasons are structured through `ExcludedReason`, scoring evidence through `RankingSignals`, human-readable scoring explanations through `ranking_reasons_ko`, and per-step execution results through `PreprocessingStepMetrics`.

The preprocessing `ArticleCandidate` is the Writer input packet. It does not generate summaries or insights; it only provides identifiers and evidence that the Writer Agent can use to decide publication and editorial content.

## Enrichment

Enrichment is a separate stage that prepares source evidence only for candidates limited by the Preprocessor. `ContentEnricher` runs a `BaseEnrichmentStep` pipeline. Fetchers, extractors, chunkers, and token counters use Strategy; factories select implementations; token budgets use Policy; and cached results use Repository.

1. Record source fetch results and final URLs.
2. Extract content while preserving headings, sections, code, tables, and list structure.
3. Select `full_content`, `chunk_selection`, or `evidence_selection` based on extracted token count and structure.
4. Use `feed_metadata_only` fallback or fail according to policy when extraction is unavailable.
5. Never store full source text or selected chunk text in trace history.

Enrichment statuses are `enriched`, `fallback`, `skipped`, and `failed`. Agent input strategies are `full_content`, `chunk_selection`, `evidence_selection`, `feed_metadata_only`, and `none`. The trace records HTTP status, MIME type, response size, durations, extractor and policy versions, cache usage, document type, extracted and selected token counts, structure counts, title similarity, quality score, and failure reason per candidate.

The initial policy treats fewer than 100 tokens as insufficient, uses full content through 4,000 tokens, routes 4,001–8,000 tokens to `chunk_selection`, and routes larger documents to `evidence_selection`. The latter strategies do not make heuristic evidence selections before an Agent selector is connected.

```bash
make enrich
make enrich DATE=2026-06-23
make trace-enrich
```

Outputs:

```text
.var/local/enriched/YYYY-MM-DD/
└── enrichment.json

.var/local/enrichment-cache/
└── {cache_key}.json
```

## Writer

The Writer currently receives `ArticleCandidate` objects from the Preprocessor and turns them into documentation output. Once Enrichment is connected, Writer will receive candidates augmented with source evidence. Writer contains Agent and Generator responsibilities.

- Writer Agent selects candidates and creates editorial results.
- Writer Generator only writes Markdown from Agent results.
- Writer updates the `briefed_articles` state and cumulative indexes after all Markdown generation succeeds.
- Main and service indexes use the accumulated `briefed_articles` state to show both priority briefings and the full cumulative list.
- GitHub Actions commits generated `docs/` files and `data/briefed_articles.json` back to `main` so later runs can use them for duplicate filtering.
- The default implementation uses `DraftNewsEditorAgent`. The Draft Agent does not generate summaries, why-it-matters text, or developer insights; it only creates `editorial_status=draft` documents.
- Use `TODAYINTECH_WRITER_AGENT=openai` to enable `OpenAINewsEditorAgent` with structured output for publish decisions, publish/reject rationale, confidence score, summary scope, evidence basis, and a natural long-form Korean summary.
- Public article pages show only the cohesive two-to-three-paragraph summary and source link. Publish rationale, confidence, evidence scope, and evidence lists remain in Writer traces.
- The OpenAI Agent does not perform full text crawling. It only uses candidate title, feed summary, tags, metadata, and ranking signals.

Writer execution:

```bash
make write
make write DATE=2026-06-07 PROCESSED_DIR=.var/local/processed OUTPUT_DIR=docs
make write WRITER_AGENT=openai
make generate-openai
```

## News Editor Agent

The Agent selects meaningful new candidates and generates one detailed briefing per selected source article. An already briefed source URL must not be processed again.

## Generator

The Generator stage writes processed results as Markdown.

1. Generate article-level briefing documents as natural editorial articles.
2. Regenerate service index documents.
3. Regenerate the main index page.
4. Record internal article/service links and original source links together.

Recommended individual article structure:

```text
# Source article title

> Service name · Published date · Category

Source link

Natural paragraph explaining the article's subject and context

Connected paragraph explaining the central content and technical significance
```

Draft documents must not generate summaries or importance claims. They only show pending status, feed summary, and candidate evidence.

Generated paths:

```text
docs/index.md
docs/services/{service_key}.md
docs/services/{service_key}/{slug}.md
```

## Build

Docusaurus builds Markdown under `docs/` into a static site.

Local build:

```bash
make build
```

Development server:

```bash
make serve
make serve HOST=127.0.0.1 PORT=3000
```

Preview built output:

```bash
make serve-build
```

## Deploy

GitHub Actions collects daily source snapshots, processes new candidates, updates archive documents, and deploys the site.

Workflow:

1. Repository checkout
2. Python 3.14 setup
3. Node 20 setup
4. Python dependency install
5. Node dependency install
6. Tests and operational trace through `make ci-quality`
7. Publish trace results to the `tracing-history` branch
8. Collection, preprocessing, and OpenAI Writer document generation through `make generate-openai`
9. Docusaurus build through `make build`
10. GitHub Pages artifact upload
11. GitHub Pages deploy

GitHub Actions automatic deployment requires the `OPENAI_API_KEY` repository secret.

Manual deployment:

```bash
make deploy
make deploy DATE=2026-06-07
make deploy-status
```
