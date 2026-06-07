PYTHON ?= .venv/bin/python
NPM ?= npm
GH ?= gh
BRANCH ?= main

SERVICE ?=
DATE ?=
COUNT ?=
OUTPUT_DIR ?=

COLLECT_ARGS :=
ifneq ($(strip $(SERVICE)),)
COLLECT_ARGS += --service $(SERVICE)
endif
ifneq ($(strip $(DATE)),)
COLLECT_ARGS += --date $(DATE)
endif
ifneq ($(strip $(COUNT)),)
COLLECT_ARGS += --preview-limit $(COUNT)
endif
ifneq ($(strip $(OUTPUT_DIR)),)
COLLECT_ARGS += --output-dir $(OUTPUT_DIR)
endif

WORKFLOW_ARGS := --ref $(BRANCH)
ifneq ($(strip $(DATE)),)
WORKFLOW_ARGS += -f target_date=$(DATE)
endif

.PHONY: help collect generate lint lint-fix format format-check check build verify ci deploy deploy-status

help:
	@echo "Today in Tech project commands"
	@echo ""
	@echo "Collection:"
	@echo "  make collect"
	@echo "  make collect SERVICE=hacker-news"
	@echo "  make collect SERVICE=hacker-news DATE=2026-06-07 COUNT=5"
	@echo "  make collect OUTPUT_DIR=data/raw-local"
	@echo ""
	@echo "Quality:"
	@echo "  make lint"
	@echo "  make lint-fix"
	@echo "  make format"
	@echo "  make format-check"
	@echo "  make check"
	@echo "  make build"
	@echo "  make verify"
	@echo ""
	@echo "GitHub deployment:"
	@echo "  make deploy"
	@echo "  make deploy DATE=2026-06-07 BRANCH=main"
	@echo "  make deploy-status"
	@echo ""
	@echo "Variables:"
	@echo "  PYTHON      Python executable path. Default: .venv/bin/python"
	@echo "  NPM         npm executable path. Default: npm"
	@echo "  GH          GitHub CLI executable path. Default: gh"
	@echo "  BRANCH      GitHub workflow ref. Default: main"
	@echo "  SERVICE     Optional service key. Default: all services"
	@echo "  DATE        Optional target date. Default: TODAYINTECH_TARGET_DATE or today"
	@echo "  COUNT       Optional preview article count. Default: collector CLI default"
	@echo "  OUTPUT_DIR  Optional raw output root. Default: TODAYINTECH_RAW_OUTPUT_DIR or data/raw"

collect:
	$(PYTHON) -m src.collection $(COLLECT_ARGS)

generate:
	$(PYTHON) -m src.main

lint:
	$(PYTHON) -m ruff check .

lint-fix:
	$(PYTHON) -m ruff check . --fix

format:
	$(PYTHON) -m ruff format .

format-check:
	$(PYTHON) -m ruff format --check .

check: lint format-check

build:
	$(NPM) run build

verify: check build

ci: verify

deploy:
	$(GH) workflow run daily-briefing.yml $(WORKFLOW_ARGS)

deploy-status:
	$(GH) run list --workflow daily-briefing.yml --limit 5
