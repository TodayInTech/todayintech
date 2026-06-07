# QUALITY

This document defines the development verification and operational tracing flow for Today in Tech.

## Concept Boundaries

- `test`: verifies code behavior with fixtures and contracts.
- `trace`: records real operational collector execution results and durations.
- `quality`: runs `test` and `trace` together to produce deployment decision evidence.

## Make Commands

```bash
make test
make test-unit
make test-collection
make trace-collect
make quality
```

## Artifacts

```text
reports/
└── junit.xml

data/traces/YYYY-MM-DD/
├── collection.json
└── summary.md
```

`reports/` and `data/traces/` are not committed to Git. GitHub Actions uploads them as artifacts.

## Current Metrics

- Collection stage status
- Total collection duration
- Service-level status
- Service-level collector strategy
- Service-level article count
- Service-level duration
- Average duration per article
- Warning codes
- Error message

## Operating Rules

- Fixture-based `make test` is for stable development verification.
- `make trace-collect` calls real external sources and is for operational tracing.
- Trace duration is not used as a strict pass/fail condition because external network conditions can affect it.
- A service with zero articles records an `empty_collection` warning.
