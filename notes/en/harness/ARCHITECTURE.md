# ARCHITECTURE

## Project Architecture

Today in Tech separates collection, preprocessing, agent editing, generation, build, and deployment. Each stage should be independently testable, and adding a service must not require changing the whole pipeline.

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
News Editor Agent
    ↓
Article Markdown Generation
    ↓
Service Index Generation
    ↓
Main Index Generation
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
│   ├── news_preprocessor.py
│   ├── briefed_article_store.py
│   ├── article_candidate.py
│   ├── url_normalizer.py
│   ├── deduplicator.py
│   ├── classifier.py
│   ├── scorer.py
│   └── summarizer.py
├── generator/
│   ├── article_markdown_writer.py
│   ├── service_markdown_writer.py
│   └── summary_markdown_writer.py
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
│   ├── github-blog.md
│   ├── google-blog.md
│   ├── openai-blog.md
│   └── anthropic-blog.md
└── articles/
    ├── hacker-news/
    ├── github-blog/
    ├── google-blog/
    ├── openai-blog/
    └── anthropic-blog/
```

`index.md` is the entry point for cross-service highlights. `services/*.md` files are service-level indexes. `articles/{service_key}/*.md` files are detailed briefings for individual source articles.

## Step-by-Step Flow

```text
Collector
    ↓
Preprocessor
    ↓
News Editor Agent
    ↓
Generator
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
7. Generate preprocessing trace output.

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

Preprocessing uses a `Pipeline + Strategy + Repository` combination. `NewsPreprocessor` runs ordered `PreprocessingStep` objects, candidate scoring is kept as a replaceable scorer strategy, and `BriefedArticleStore` acts as the state repository for source articles that have already been briefed.

## News Editor Agent

The Agent selects meaningful new candidates and generates one detailed briefing per selected source article. An already briefed source URL must not be processed again.

## Generator

The Generator stage writes processed results as Markdown.

1. Generate article-level briefing documents.
2. Regenerate service index documents.
3. Regenerate the main index page.
4. Record internal article/service links and original source links together.

Generated paths:

```text
docs/index.md
docs/services/{service_key}.md
docs/articles/{service_key}/{slug}.md
```

## Build

Docusaurus builds Markdown under `docs/` into a static site.

Local build:

```bash
make build
```

Development server:

```bash
npm run start -- --host 127.0.0.1 --port 3000
```

## Deploy

GitHub Actions collects daily source snapshots, processes new candidates, updates archive documents, and deploys the site.

Workflow:

1. Repository checkout
2. Python 3.14 setup
3. Node 20 setup
4. Python dependency install
5. Node dependency install
6. Collection, preprocessing, and Markdown scaffold generation through `make generate`
7. Docusaurus build through `make build`
8. GitHub Pages artifact upload
9. GitHub Pages deploy

Manual deployment:

```bash
make deploy
make deploy DATE=2026-06-07
make deploy-status
```
