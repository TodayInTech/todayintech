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

Service implementations must use Factory Method and Abstract Factory patterns so new services can be added without changing the main pipeline.

Recommended structure:

```text
src/
├── services/
│   ├── base.py
│   ├── factory.py
│   ├── hacker_news.py
│   ├── github_blog.py
│   ├── google_blog.py
│   ├── openai_blog.py
│   └── anthropic_blog.py
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

1. Create services through the factory.
2. Collect RSS/Atom feeds.
3. Normalize articles.
4. Deduplicate through canonical URLs and `seen.json`.
5. Score and classify stories.
6. Generate `docs/{YYYY-MM-DD}/services/{service}.md` files.
7. Generate `docs/{YYYY-MM-DD}/summary.md`.
8. Build Docusaurus.
9. Deploy to GitHub Pages through GitHub Actions.
