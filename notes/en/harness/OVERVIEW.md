# OVERVIEW

## Project Purpose

Today in Tech is a technology article curation archive that collects RSS/Atom feeds and official sitemaps every day, then uses an AI-based News Editor Agent to select meaningful articles over a period and publish them as a static documentation site.

This project is not a simple RSS reader and no longer treats every day as a separate newsletter. The Collector stores daily source snapshots, but the Agent must not regenerate articles that have already been briefed. Users start from the main page, then move into service pages and article-level briefings.

## Core Goals

- Collect latest source snapshots every day.
- Select only meaningful new article candidates.
- Generate one detailed briefing document per selected source article.
- Maintain service-level article archives and the main index page.
- Preserve original source links and internal article/service links.
- Publish through a Docusaurus-based static site.

## MVP Scope

The MVP focuses on:

- RSS/Atom Feed Collection
- News Normalization
- Preprocessing / Deduplication
- Briefed Article Filtering
- Candidate Ranking
- Importance Scoring
- Category Classification
- Markdown Generation
- Docusaurus Build
- GitHub Pages Deployment

High-quality LLM-based summarization and importance scoring will be strengthened later. The current scaffold prioritizes heuristic processing and the Markdown generation structure.

## Language Policy

- Root documents and harness documents are written in Korean by default.
- English documents are maintained under `notes/en/`.
- Automatically generated briefings use Korean as the default output language.

## Harness Tracking Documents

- `notes/en/harness/TASKS.md`: tracks project stages and complete/in-progress checklists.
- `notes/en/harness/service/SERVICES.md`: tracks currently supported services, collection methods, and collection scopes.
- `notes/en/harness/ARCHITECTURE.md`: explains the overall architecture and stage flow.
- `notes/en/harness/TECH_STACK.md`: explains the confirmed technology stack and operating standards.
- `notes/en/harness/ENV.md`: tracks environment variables and `SETTINGS` singleton usage rules.
- `notes/en/harness/QUALITY.md`: explains development verification and operational tracing artifacts.
- `notes/en/harness/COMMIT_MESSAGE.md`: defines commit message rules.

When service implementations or collector strategies change, check and update `notes/en/harness/service/SERVICES.md` at the same time.
When implementation status changes, update the checklist status in `notes/en/harness/TASKS.md`.
