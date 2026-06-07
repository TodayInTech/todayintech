# TASKS

This document tracks the current work status for Today in Tech.
Update it continuously when feature implementation, documentation structure, collector strategies, or deployment flow changes.

## Status Rules

- `[x]`: complete
- `[ ]`: incomplete
- `In progress`: currently being worked on and must not be marked complete yet
- `Pending`: planned for a later stage

## Current Stage

The project has completed `Project Init` and is currently working on the `Collector` stage.

## Work Checklist

- [x] Project Init - complete
  - Python 3.14 project setup
  - Docusaurus static documentation site scaffold
  - Draft GitHub Actions / GitHub Pages deployment flow
  - Initial README, AGENTS, and harness documents
  - Korean root documents and English `notes/en/` document structure

- [ ] Collector - in progress
  - [x] Source metadata implementations separated
  - [x] `sources` and `collection` top-level package boundary separated
  - [x] `NewsSourceFactory` source creation structure
  - [x] `CollectorStrategyFactory` collector strategy creation structure
  - [x] RSS collector implementation
  - [x] Sitemap collector implementation
  - [x] Service-level raw JSON output structure
  - [x] Standalone collector CLI
  - [x] Service-level collection condition documentation
  - [ ] Persistent deduplication through `seen.json`
  - [ ] Collector tests

- [ ] Processing - pending
  - Deduplication improvements
  - Importance scoring
  - Category classification
  - LLM summarization integration

- [ ] Generator - pending
  - Improve service-level Markdown generation
  - Improve global summary Markdown generation
  - Verify internal links and source links

- [ ] Build / Deploy - pending
  - Validate Docusaurus build
  - Validate actual GitHub Actions deployment
  - Validate GitHub Pages production settings

## Next Work Candidates

- Connect `seen.json` storage with collector deduplication
- Add collector unit tests
- Define Anthropic sitemap collector timeout, limit, and metadata fallback policy
- Stabilize raw JSON schema
