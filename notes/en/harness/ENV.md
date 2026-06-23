# ENV

This document tracks the environment variables used by Today in Tech.
When an environment variable is added, removed, or renamed, update `.env.example`, `src/settings.py`, this document, and `harness/ENV.md` together.

## Maintenance Rules

- Environment variable examples live in `.env.example`.
- Runtime code must use the `SETTINGS` singleton from `src/settings.py` instead of calling `os.getenv()` directly.
- `SETTINGS = AppSettings.from_env()` first loads the root `.env` file and then reads environment variables at import time.
- Existing shell environment variables are not overwritten by `.env` values.
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
| `TODAYINTECH_RAW_OUTPUT_DIR` | `.var/local/raw` | Optional | `raw_output_dir` | Root directory for collector raw JSON output |
| `TODAYINTECH_PROCESSED_OUTPUT_DIR` | `.var/local/processed` | Optional | `processed_output_dir` | Root directory for preprocessor candidate JSON output |
| `TODAYINTECH_ENRICHED_OUTPUT_DIR` | `.var/local/enriched` | Optional | `enriched_output_dir` | Root directory for enrichment result JSON output |
| `TODAYINTECH_ENRICHMENT_CACHE_DIR` | `.var/local/enrichment-cache` | Optional | `enrichment_cache_dir` | JSON cache versioned by URL, extractor, chunker, and policy settings |
| `TODAYINTECH_TRACE_OUTPUT_DIR` | `.var/local/traces` | Optional | `trace_output_dir` | Root directory for operational trace JSON/Markdown output |
| `TODAYINTECH_BRIEFED_ARTICLES_PATH` | `data/briefed_articles.json` | Optional | `briefed_articles_path` | State file path for source articles already briefed or published |
| `TODAYINTECH_WRITER_AGENT` | `draft` | Optional | `writer_agent` | Writer Agent implementation. Use `draft` or `openai`. `openai` requires `OPENAI_API_KEY` |
| `TODAYINTECH_MAX_ARTICLES_PER_SERVICE` | `5` | Optional | `max_articles_per_service` | Legacy Markdown scaffold article limit per service. Not used by the current Writer path |
| `TODAYINTECH_MAX_CANDIDATES_PER_SERVICE` | `10` | Optional | `max_candidates_per_service` | Maximum preprocessor candidates kept per service for Agent input. Minimum is 1 |
| `TODAYINTECH_MAX_CANDIDATES_TOTAL` | `50` | Optional | `max_candidates_total` | Maximum preprocessor candidates kept across all services for Agent input. Minimum is 1 |
| `TODAYINTECH_ENRICHMENT_TIMEOUT_SECONDS` | `20` | Optional | `enrichment_timeout_seconds` | Source HTTP request timeout in seconds |
| `TODAYINTECH_ENRICHMENT_MAX_ATTEMPTS` | `2` | Optional | `enrichment_max_attempts` | Maximum source request attempts for timeout or network errors |
| `TODAYINTECH_ENRICHMENT_MINIMUM_TOKENS` | `100` | Optional | `enrichment_minimum_tokens` | Minimum token count for usable extracted content |
| `TODAYINTECH_ENRICHMENT_FULL_CONTENT_MAX_TOKENS` | `4000` | Optional | `enrichment_full_content_max_tokens` | Maximum token count for direct full-content Agent input |
| `TODAYINTECH_ENRICHMENT_CHUNK_SELECTION_MAX_TOKENS` | `8000` | Optional | `enrichment_chunk_selection_max_tokens` | Token boundary between chunk selection and evidence selection |
| `TODAYINTECH_ENRICHMENT_CHUNK_MAX_TOKENS` | `1200` | Optional | `enrichment_chunk_max_tokens` | Target maximum token count per structural chunk |
| `TODAYINTECH_ENRICHMENT_SELECTED_CHUNKS_MAX_TOKENS` | `4000` | Optional | `enrichment_selected_chunks_max_tokens` | Maximum selected chunk token count passed to Writer for long-form content |

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

- `src/main.py`: Collector, Preprocessor, Enrichment, and Writer paths plus enrichment policy settings
- `src/collection/__main__.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.raw_output_dir`
- `src/processing/__main__.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.raw_output_dir`, `SETTINGS.processed_output_dir`, `SETTINGS.briefed_articles_path`, `SETTINGS.max_candidates_per_service`, `SETTINGS.max_candidates_total`
- `src/enrichment/__main__.py`: enrichment output/cache paths, HTTP request, token budget, and chunk size settings
- `src/writer/__main__.py`: target date, Writer Agent settings, `enriched_output_dir`, output path, and briefed state

## Addition Checklist

- [ ] Add the variable to `.env.example` with section comments
- [ ] Add the field and `from_env()` mapping to `src/settings.py`
- [ ] Update this document's variable tables
- [ ] Update `harness/ENV.md` at the same time
- [ ] Update README and GitHub Actions secret documentation when needed
