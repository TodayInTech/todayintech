# TASKS

This document tracks the current work status for Today in Tech.
Update it continuously when feature implementation, documentation structure, collector strategies, or deployment flow changes.

## Status Rules

- `[x]`: complete
- `[ ]`: incomplete
- `In progress`: currently being worked on and must not be marked complete yet
- `Pending`: planned for a later stage

## Current Stage

The project has completed the `Project Init`, `Collector`, and `Preprocessor` stages and is currently building the basic `Writer` structure. The product direction has changed from dated daily briefings to an article-level cumulative curation archive.

## Work Checklist

- [x] Project Init - complete
  - Python 3.14 project setup
  - Docusaurus static documentation site scaffold
  - Draft GitHub Actions / GitHub Pages deployment flow
  - Initial README, AGENTS, and harness documents
  - Korean root documents and English `notes/en/` document structure

- [x] Collector - complete
  - [x] Source metadata implementations separated
  - [x] `sources` and `collection` top-level package boundary separated
  - [x] `NewsSourceFactory` source creation structure
  - [x] `CollectorStrategyFactory` collector strategy creation structure
  - [x] RSS collector implementation
  - [x] Sitemap collector implementation
  - [x] Service-level raw JSON output structure
  - [x] Standalone collector CLI
  - [x] Makefile-based collector command
  - [x] Makefile-based lint, format, build, and verify commands
  - [x] Makefile-based manual GitHub Actions deployment trigger
  - [x] Minimal test flow and operational trace artifacts
  - [x] `tracing-history` branch flow for accumulated operational traces
  - [x] Operations dashboard data and UI from remote trace history
  - [x] Service-level collection condition documentation
  - [x] Basic collector contract tests
  - [x] Daily snapshot collection policy documented
  - [x] RSS collector support for `collection_limit` / `lookback_days` source settings
  - [x] Hacker News points/comments/rank metadata extraction

- [x] Preprocessor - complete
  - [x] URL canonicalization
  - [x] Required field validation
  - [x] Run-level URL/title fingerprint deduplication
  - [x] Exclude already published articles through `briefed_articles`
  - [x] Candidate ranking and agent input limiting
  - [x] Generate Writer-facing `candidate_id`, `url_hash`, `suggested_doc_key`, and `suggested_article_path`
  - [x] Preprocessing trace output
  - [x] Standalone Preprocessor CLI
  - [x] Makefile-based preprocessor command
  - [x] Connect the Preprocessor stage after the Collector stage in `src.main`
  - [x] Connect Writer draft generation to `briefed_articles` state updates
  - [x] Restructure the preprocessing package around contracts/steps/scoring/state to match the Collector structure
  - [x] Add preprocessing pipeline factory, scorer ABC, exclusion reason enum, ranking signal model, step metrics, context helpers, and remove legacy helpers
  - [x] Add service preprocessing policies, candidate quality gate, and scoring explanations
  - [x] Make candidate scoring use the `generated_for` date instead of the workflow execution time

- [ ] Enrichment - in progress
  - [x] Define enrichment statuses and Agent input strategies
  - [x] Define the source fetch, extraction, structure, token, and failure trace contract
  - [x] Implement overall/service-level aggregation and JSON/Markdown trace writers
  - [x] Implement the HTTP fetcher and Trafilatura HTML extractor
  - [x] Implement structure-preserving chunking and adaptive token-budget policy
  - [x] Add the enrichment pipeline factory, JSON cache, storage, and standalone CLI
  - [x] Implement structure-based chunk/evidence selection
  - [x] Connect Writer input and the full pipeline

- [ ] Writer - in progress
  - [x] Add Writer package structure
  - [x] Implement Draft Agent contract/schema
  - [x] Generate `docs/services/{service_key}/{slug}.md` draft documents
  - [x] Add natural editorial briefing template for individual article documents
  - [x] Generate `docs/services/{service_key}.md` service indexes
  - [x] Generate `docs/index.md` main page
  - [x] Update `briefed_articles` draft state after successful generation
  - [x] Add standalone Writer CLI and Makefile command
  - [x] Implement OpenAI-based News Editor Agent
  - [x] Add Writer Agent selection setting
  - [x] Add official service brand icons and service-index rendering
  - [x] Add a Today in Tech SVG brand icon and theme-aware UI integration
  - [x] Apply the brand asset to the README and organization icon usage
  - [x] Generate PNG brand assets for organization icon uploads
  - [x] Add publish rationale, evidence scope, and confidence fields to the OpenAI Agent decision schema
  - [x] Simplify public article pages around a natural long-form Korean summary
  - [x] Apply OpenAI Agent summary length guidance by Enrichment input strategy
  - [x] Add card-based briefing navigation UI for main and service pages
  - [x] Add Docusaurus English locale generation for main, service, and operations docs
  - [ ] Implement publication status transition policy

- [x] Build / Deploy - complete
  - Validate Docusaurus build
  - Validate actual GitHub Actions deployment
  - Validate GitHub Pages production settings
  - Add a Static Pages Deploy workflow that deploys committed static docs and remote trace operations data without running the Agent

## Next Work Candidates

- Refine Agent-based chunk/evidence selection
- Persist enrichment cache and optimize GitHub Actions cost
- Add Agent claim-evidence validation
