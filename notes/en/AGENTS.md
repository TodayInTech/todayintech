# AGENTS.md

Today in Tech is an AI-curated technology news briefing platform. It collects RSS/Atom feeds, selects important stories through a News Editor Agent, generates service-level Markdown briefings, and publishes them through a static documentation site.

This English document mirrors the Korean root `AGENTS.md`. The Korean root document is the source of truth.

## Fixed Framework

- Runtime: Python 3.14
- Static Site: Docusaurus
- Language: Korean at the repository root, English under `notes/en/`
- Storage: JSON files
- Automation: GitHub Actions
- Hosting: GitHub Pages
- LLM: OpenAI API

## MVP Services

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

## Architecture Rules

The project must generate one briefing bundle per date. Each dated bundle contains one Markdown briefing per service and one global summary Markdown file that links to service pages and original sources.

Service creation uses Factory Method and Abstract Factory, while collection algorithms are separated through the Strategy pattern. Services that do not provide RSS must use an official collector strategy such as sitemap, official API, or HTML metadata collection.

Product and documentation language uses `service` for the briefing unit exposed to users. Code uses `source` for external collection targets and `collection` for the execution layer.

Recommended structure:

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
├── generator/
├── models/
└── main.py
```

Generated document structure:

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

## Agent Rules

The News Editor Agent evaluates importance, classifies categories, assists deduplication, summarizes service-level news, and generates domain-level insights for the global summary.

The agent must not rewrite full articles, invent unsupported facts, include every collected article, or omit source links.

## Publishing Flow

Each stage must remain independently executable for development and debugging.

- Run the Collector stage with `make collect`.
- Inspect one service with `make collect SERVICE={service_key}`.
- The Collector stage only writes `data/raw/{YYYY-MM-DD}/summary.json` and `data/raw/{YYYY-MM-DD}/services/{service}.json`; it does not generate Markdown or build Docusaurus.
- Run the full pipeline with `.venv/bin/python -m src.main`.
- Future Processing and Generator stages should also expose independent entrypoints.

1. Create services through the factory.
2. Collect information through each service collector strategy via `NewsCollector`.
3. Normalize articles.
4. Store raw service-level results under `data/raw/{YYYY-MM-DD}/services/{service}.json`.
5. Deduplicate through canonical URLs and `seen.json`.
6. Score and classify stories.
7. Generate `docs/{YYYY-MM-DD}/services/{service}.md` files.
8. Generate `docs/{YYYY-MM-DD}/summary.md`.
9. Build Docusaurus.
10. Deploy to GitHub Pages through GitHub Actions.

## Maintenance Rules

- Keep Korean root documents as the primary documentation.
- Update supported language documents in the same change.
- English documents live under `notes/en/`.
- When task status changes, update `harness/TASKS.md` and `notes/en/harness/TASKS.md`.
- When service collection methods or collection scopes change, update `harness/service/SERVICES.md` and `notes/en/harness/service/SERVICES.md`.
