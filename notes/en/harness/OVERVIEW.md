# OVERVIEW

## Project Purpose

Today in Tech is a technology news briefing platform that collects RSS/Atom feeds and uses an AI-based News Editor Agent to select important stories for publication as a static documentation site.

This project is not a simple RSS reader. It does not store or list every article. Instead, it generates service-level briefings and a global summary so developers and technology leaders can quickly understand the day's core technology trends.

## Core Goals

- Collect the latest technology news every day.
- Select important stories per service.
- Provide domain-level implications in the global summary.
- Preserve both original source links and internal service document links.
- Publish through a Docusaurus-based static site.

## MVP Scope

The MVP focuses on:

- RSS/Atom Feed Collection
- News Normalization
- Deduplication
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
- `notes/en/harness/COMMIT_MESSAGE.md`: defines commit message rules.

When service implementations or collector strategies change, check and update `notes/en/harness/service/SERVICES.md` at the same time.
When implementation status changes, update the checklist status in `notes/en/harness/TASKS.md`.
