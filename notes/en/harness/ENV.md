# ENV

This document tracks the environment variables used by Today in Tech.
When an environment variable is added, removed, or renamed, update `.env.example`, `src/settings.py`, this document, and `harness/ENV.md` together.

## Maintenance Rules

- Environment variable examples live in `.env.example`.
- Runtime code must use the `SETTINGS` singleton from `src/settings.py` instead of calling `os.getenv()` directly.
- `SETTINGS = AppSettings.from_env()` reads environment variables at import time.
- Empty strings are treated as `None` for optional values.
- Numeric environment variables are parsed by `SETTINGS` and receive fallback defaults.

## OpenAI / LLM Settings

| Variable | Default | Required | SETTINGS Field | Description |
| --- | --- | --- | --- | --- |
| `OPENAI_API_KEY` | none | Required when LLM features are enabled | `openai_api_key` | OpenAI API key for importance scoring, summarization, and insight generation |
| `OPENAI_MODEL` | `gpt-5-mini` | Optional | `openai_model` | Model used by the LLM agent |

## Pipeline Settings

| Variable | Default | Required | SETTINGS Field | Description |
| --- | --- | --- | --- | --- |
| `TODAYINTECH_TIMEZONE` | `Asia/Seoul` | Optional | `timezone` | Briefing reference timezone |
| `TODAYINTECH_OUTPUT_DIR` | `docs` | Optional | `output_dir` | Root directory for generated Markdown briefings |
| `TODAYINTECH_RAW_OUTPUT_DIR` | `data/raw` | Optional | `raw_output_dir` | Root directory for collector raw JSON output |
| `TODAYINTECH_MAX_ARTICLES_PER_SERVICE` | `5` | Optional | `max_articles_per_service` | Maximum number of articles summarized per service during Markdown generation. Minimum is 1 |

## Local Reproducibility Settings

| Variable | Default | Required | SETTINGS Field | Description |
| --- | --- | --- | --- | --- |
| `TODAYINTECH_TARGET_DATE` | today's date | Optional | `target_date` | `YYYY-MM-DD` value for reproducible local runs or dated output generation |

## Docusaurus / GitHub Pages Settings

| Variable | Default | Required | SETTINGS Field | Description |
| --- | --- | --- | --- | --- |
| `DOCUSAURUS_URL` | `https://example.com` | Required for deployment | `docusaurus_url` | Docusaurus site URL |
| `DOCUSAURUS_BASE_URL` | `/` | Required for deployment | `docusaurus_base_url` | GitHub Pages base URL for subpath deployment |

## Current Code Usage

- `src/main.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.max_articles_per_service`, `SETTINGS.output_dir`, `SETTINGS.raw_output_dir`
- `src/collection/__main__.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.raw_output_dir`

## Addition Checklist

- [ ] Add the variable to `.env.example` with section comments
- [ ] Add the field and `from_env()` mapping to `src/settings.py`
- [ ] Update this document's variable tables
- [ ] Update `harness/ENV.md` at the same time
- [ ] Update README and GitHub Actions secret documentation when needed
