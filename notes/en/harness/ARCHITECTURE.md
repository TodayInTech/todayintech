# ARCHITECTURE

## Project Architecture

Today in Tech separates collection, processing, generation, build, and deployment. Each stage should be independently testable, and adding a service must not require changing the whole pipeline.

```text
Official Sources
    ↓
Service Factory
    ↓
Service-specific Collector Strategy
    ↓
Normalize Articles
    ↓
Deduplicate
    ↓
Importance Scoring
    ↓
Category Classification
    ↓
Summarization
    ↓
Service Markdown Generation
    ↓
Global Summary Markdown Generation
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
│   ├── deduplicator.py
│   ├── classifier.py
│   ├── scorer.py
│   └── summarizer.py
├── generator/
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

Each date produces one briefing bundle.

```text
docs/
└── YYYY-MM-DD/
    ├── summary.md
    └── services/
        ├── hacker-news.md
        ├── github-blog.md
        ├── google-blog.md
        ├── openai-blog.md
        └── anthropic-blog.md
```

`summary.md` is the entry point for the global briefing. `services/*.md` files are service-level detail pages.

## Step-by-Step Flow

```text
Collector
    ↓
Processing
    ↓
Generator
    ↓
Build
    ↓
Deploy
```

## Collector

The Collector stage must be independently executable and make service-level collection results easy to inspect.

1. `NewsCollector` creates MVP service implementations through `NewsSourceFactory`.
2. Each service implementation collects information through its own collector strategy, such as RSS/Atom, sitemap, or official API.
3. Feed entries are normalized into the shared `Article` model.
4. Service-level collection results are wrapped as `ServiceCollectionResult`.
5. URL, title, publication date, source, summary, and tags are preserved where possible.
6. Collection results are stored as JSON under `data/raw/{YYYY-MM-DD}/`.

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

Available service keys are exposed through `NewsSourceFactory.service_keys()`. The collector CLI prints a console summary and writes the same results to `data/raw/{YYYY-MM-DD}/summary.json` and `data/raw/{YYYY-MM-DD}/services/{service}.json`. This stage does not generate Markdown or build Docusaurus.

MVP services:

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

Raw collection output:

```text
data/raw/YYYY-MM-DD/
├── summary.json
└── services/
    ├── hacker-news.json
    ├── github-blog.json
    ├── google-blog.json
    ├── openai-blog.json
    └── anthropic-blog.json
```

## Processing

The Processing stage prepares collected articles as briefing candidates.

1. Remove duplicates by URL.
2. Classify article categories.
3. Calculate importance scores.
4. Create summary data.

The current scaffold is heuristic-based. The LLM-based News Editor Agent will be connected to this layer later.

## Generator

The Generator stage writes processed results as Markdown.

1. Generate service-level documents.
2. Generate the global summary document.
3. Record internal service document links and original source links together.

Generated paths:

```text
docs/{YYYY-MM-DD}/summary.md
docs/{YYYY-MM-DD}/services/{service}.md
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

GitHub Actions generates and deploys the briefing every day.

Workflow:

1. Repository checkout
2. Python 3.14 setup
3. Node 20 setup
4. Python dependency install
5. Node dependency install
6. Briefing generation through `make generate`
7. Docusaurus build through `make build`
8. GitHub Pages artifact upload
9. GitHub Pages deploy

Manual deployment:

```bash
make deploy
make deploy DATE=2026-06-07
make deploy-status
```
