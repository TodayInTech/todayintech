# ARCHITECTURE

## Project Architecture

Today in Tech separates collection, processing, generation, build, and deployment. Each stage should be independently testable, and adding a service must not require changing the whole pipeline.

```text
RSS/Atom Sources
    ↓
Service Factory
    ↓
Service-specific Collector
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
├── services/
│   ├── base.py
│   ├── factory.py
│   ├── rss_service.py
│   ├── hacker_news.py
│   ├── github_blog.py
│   ├── google_blog.py
│   ├── openai_blog.py
│   └── anthropic_blog.py
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

Service implementations follow Factory Method and Abstract Factory patterns.

- `BaseNewsService`: common interface for every news service implementation
- `RssNewsService`: default implementation for RSS/Atom services
- `NewsServiceFactory`: creates concrete services by service key
- `AbstractNewsServiceFactory`: abstract factory for future service family expansion

When adding a new service, do not modify the existing pipeline. Add an implementation under `src/services/` and register it in the factory registry.

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

The Collector stage is handled by service implementations.

1. `NewsServiceFactory` creates MVP service implementations.
2. Each service implementation collects RSS/Atom feeds.
3. Feed entries are normalized into the shared `Article` model.
4. URL, title, publication date, source, summary, and tags are preserved where possible.

MVP services:

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

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
npm run build
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
6. Briefing generation
7. Docusaurus build
8. GitHub Pages artifact upload
9. GitHub Pages deploy
