# TECH_STACK

## Runtime

- Python 3.14
- Node.js 20

The Python version must remain consistent across `.python-version` and GitHub Actions.

## Python Libraries

- `feedparser`: RSS/Atom parsing
- `httpx`: HTTP requests
- `pydantic`: data model validation
- `openai`: LLM API integration
- `jinja2`: future Markdown template rendering extension
- `ruff`: Python linting and formatting

## Static Site

- Docusaurus
- React
- GitHub Pages

Docusaurus uses the `docs/` directory as the documentation root. The Python pipeline generates briefing Markdown files, and Docusaurus builds them into a static site.

## Automation

- GitHub Actions
- Makefile

The workflow lives in `.github/workflows/daily-briefing.yml`.
Local execution, rule checks, builds, and manual GitHub Actions deployment triggers are managed by the root `Makefile`.

## Storage

- JSON file-based storage
- A `briefed_articles` state file tracks source articles that have already been briefed/published
- Raw collection data remains local under `.var/` or GitHub Actions artifacts only
- Operational traces accumulate on the `tracing-history` branch

The MVP does not use a database server, search engine, or vector database.

## Environment Variables

Environment variable examples live in `.env.example`. Variable meanings, defaults, and code usage are managed in `notes/en/harness/ENV.md`.

Main variables:

- `OPENAI_API_KEY`
- `OPENAI_MODEL`
- `TODAYINTECH_TIMEZONE`
- `TODAYINTECH_OUTPUT_DIR`
- `TODAYINTECH_RAW_OUTPUT_DIR`
- `TODAYINTECH_TRACE_OUTPUT_DIR`
- `TODAYINTECH_MAX_ARTICLES_PER_SERVICE`
- `TODAYINTECH_TARGET_DATE`
- `DOCUSAURUS_URL`
- `DOCUSAURUS_BASE_URL`
