# SERVICES

This document tracks the services currently supported by Today in Tech and how each service is collected.
When service implementations, collection conditions, or collector strategies change, update this document at the same time.

## Maintenance Rules

- Service implementations live under `src/sources/implementations/`.
- Service registration lives in `src/sources/factory.py`.
- Collection algorithms live under `src/collection/strategies/`.
- Services without RSS must not use third-party RSS feeds. Use official-source strategies such as official sitemap, official API, or HTML metadata collection.
- Inspect collection results with `.venv/bin/python -m src.collection --service {service_key}`.

## Currently Supported Services

| Service | service_key | Collection Method | Source URL | Collection Scope | Status |
| --- | --- | --- | --- | --- | --- |
| Hacker News | `hacker-news` | RSS | `https://hnrss.org/frontpage` | Normalize every item included in the frontpage RSS feed into `Article` | Supported |
| GitHub Blog | `github-blog` | RSS | `https://github.blog/feed/` | Normalize every item included in the GitHub Blog RSS feed into `Article` | Supported |
| Google Blog | `google-blog` | RSS | `https://blog.google/technology/rss/` | Normalize every item included in the Google Technology RSS feed into `Article` | Supported |
| OpenAI Blog | `openai-blog` | RSS | `https://openai.com/news/rss.xml` | Normalize every item included in the OpenAI News RSS feed into `Article` | Supported |
| Anthropic Blog | `anthropic-blog` | Sitemap + page metadata | `https://www.anthropic.com/sitemap.xml` | Include sitemap URLs whose path starts with `/news/`, sort by latest `lastmod`, and fetch page metadata for up to 20 entries | Supported |

## Collector Strategy Conditions

### RSS

- Implementation: `RssCollector`
- Services: Hacker News, GitHub Blog, Google Blog, OpenAI Blog
- Collection rules:
  - Parse `source.source_url` with feedparser.
  - Skip entries without title or link.
  - Convert published or updated values into `published_at`.
  - Preserve authors, tags, and summary when available.
  - The collector stage does not currently apply per-service feed count limits.

### Sitemap

- Implementation: `SitemapCollector`
- Service: Anthropic Blog
- Collection rules:
  - Fetch the official sitemap XML.
  - Include only URLs that match `url_prefixes`.
  - Sort entries by `lastmod` descending.
  - Fetch page metadata up to `collection_limit`.
  - Build `Article` from HTML title, og:title, description, and og:description.

## Expansion Update Checklist

- [ ] Add or update `src/sources/implementations/{source}.py`
- [ ] Add or update the `NewsSourceFactory` registry
- [ ] Add or update the required collector strategy or config
- [ ] Update this document's service table and collection scope
- [ ] Update `harness/service/SERVICES.md` at the same time
- [ ] Verify collection with single-service collector execution
