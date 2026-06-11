# TASKS

This document tracks the current work status for Today in Tech.
Update it continuously when feature implementation, documentation structure, collector strategies, or deployment flow changes.

## Status Rules

- `[x]`: complete
- `[ ]`: incomplete
- `In progress`: currently being worked on and must not be marked complete yet
- `Pending`: planned for a later stage

## Current Stage

The project has completed `Project Init` and `Collector`, and is now updating the specification from dated daily briefings to an article-level cumulative curation archive.

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
  - [x] Service-level collection condition documentation
  - [x] Basic collector contract tests
  - [x] Daily snapshot collection policy documented
  - [ ] RSS collector support for `collection_limit` / `lookback_days` source settings
  - [ ] Hacker News points/comments/rank metadata extraction

- [ ] Preprocessor - next
  - URL canonicalization
  - Required field validation
  - Run-level URL/title fingerprint deduplication
  - Exclude already published articles through `briefed_articles`
  - Candidate ranking and agent input limiting
  - Preprocessing trace output

- [ ] News Editor Agent - pending
  - Select new candidate articles
  - Generate article-level detailed briefings
  - Generate service summaries and main page insights
  - Validate LLM response schema and fallback policy

- [ ] Generator - pending
  - Generate `docs/articles/{service_key}/{slug}.md`
  - Generate `docs/services/{service_key}.md` service indexes
  - Generate `docs/index.md` main page
  - Verify internal links and source links

- [x] Build / Deploy - complete
  - Validate Docusaurus build
  - Validate actual GitHub Actions deployment
  - Validate GitHub Pages production settings

## Next Work Candidates

- Implement RSS collector source scope limits
- Design the `briefed_articles` state model
- Add Preprocessor entrypoint and trace artifacts
- Convert dated generator output into article archive output
