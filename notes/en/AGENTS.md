# AGENTS.md

Today in Tech is an AI-curated technology article archive. It collects RSS/Atom feeds and official sitemaps every day, but the News Editor Agent only briefs meaningful articles that have not already been published.

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

The project no longer treats a dated daily briefing as the primary product. Collection still runs daily as a source snapshot, but the site is organized as a cumulative archive of article briefings and service indexes.

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

## Agent Rules

The News Editor Agent acts as a curator and research editor. It selects meaningful new candidate articles, creates one article briefing per selected source article, updates service-level indexes, and contributes domain-level insights for the main page.

The agent must not rewrite full articles, invent unsupported facts, include every collected article, omit source links, or regenerate an article that already exists in the briefed article state.

## Publishing Flow

Each stage must remain independently executable for development and debugging.

- Run the Collector stage with `make collect`.
- Inspect one service with `make collect SERVICE={service_key}`.
- The Collector stage only writes `.var/local/raw/{YYYY-MM-DD}/summary.json` and `.var/local/raw/{YYYY-MM-DD}/services/{service}.json`; it does not generate Markdown or build Docusaurus.
- The Collector stores daily snapshots. Repeated articles across dates are expected and must be filtered by preprocessing, not by collection.
- Run the Preprocessor stage with `make preprocess`.
- The Preprocessor normalizes URLs, removes run-level duplicates, excludes already briefed articles, ranks candidates, and generates Writer-facing candidate identifiers.
- Run the full pipeline with `.venv/bin/python -m src.main`; it currently connects the Preprocessor after the Collector.
- Future Processing and Generator stages should also expose independent entrypoints.

1. Create services through the factory.
2. Collect information through each service collector strategy via `NewsCollector`.
3. Normalize articles.
4. Store raw service-level results under `.var/local/raw/{YYYY-MM-DD}/services/{service}.json`.
5. Normalize URLs and remove run-level duplicates in preprocessing.
6. Exclude articles already published in the briefed article state.
7. Generate Writer-facing candidates with `candidate_id`, `url_hash`, `suggested_doc_key`, and `suggested_article_path`.
8. Let the Writer Agent select meaningful new candidates and create article-level briefings.
9. Let the Writer Generator create `docs/articles/{service_key}/{slug}.md` files.
10. Regenerate `docs/services/{service_key}.md` service indexes.
11. Regenerate `docs/index.md` as the main entry page.
12. Update the briefed article state after successful generation.
13. Build Docusaurus.
14. Deploy to GitHub Pages through GitHub Actions.

## Maintenance Rules

- Keep Korean root documents as the primary documentation.
- Update supported language documents in the same change.
- English documents live under `notes/en/`.
- When task status changes, update `harness/TASKS.md` and `notes/en/harness/TASKS.md`.
- When service collection methods or collection scopes change, update `harness/service/SERVICES.md` and `notes/en/harness/service/SERVICES.md`.
