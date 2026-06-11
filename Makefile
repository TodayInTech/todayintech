PYTHON ?= .venv/bin/python
NPM ?= npm
GH ?= gh
BRANCH ?= main
TRACE_HISTORY_BRANCH ?= tracing-history
TRACE_HISTORY_DIR ?= .var/remote/tracing-history

SERVICE ?=
DATE ?=
COUNT ?=
OUTPUT_DIR ?=
RAW_DIR ?=
PROCESSED_DIR ?=
BRIEFED_STATE ?=
TRACE_DIR ?= .var/local/traces
REPORT_DIR ?= .var/local/reports
CI_RAW_DIR ?= .artifacts/raw
CI_PROCESSED_DIR ?= .artifacts/processed
CI_TRACE_DIR ?= .artifacts/traces
CI_REPORT_DIR ?= .artifacts/reports

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

PREPROCESS_ARGS :=
ifneq ($(strip $(DATE)),)
PREPROCESS_ARGS += --date $(DATE)
endif
ifneq ($(strip $(RAW_DIR)),)
PREPROCESS_ARGS += --raw-dir $(RAW_DIR)
endif
ifneq ($(strip $(PROCESSED_DIR)),)
PREPROCESS_ARGS += --output-dir $(PROCESSED_DIR)
endif
ifneq ($(strip $(BRIEFED_STATE)),)
PREPROCESS_ARGS += --briefed-state $(BRIEFED_STATE)
endif

WORKFLOW_ARGS := --ref $(BRANCH)
ifneq ($(strip $(DATE)),)
WORKFLOW_ARGS += -f target_date=$(DATE)
endif

.PHONY: help collect preprocess trace-collect trace-preprocess fetch-trace-history generate test test-unit test-collection lint lint-fix format format-check check build verify quality ci-quality ci deploy deploy-status

help:
	@echo "Today in Tech project commands"
	@echo ""
	@echo "Collection:"
	@echo "  make collect"
	@echo "  make collect SERVICE=hacker-news"
	@echo "  make collect SERVICE=hacker-news DATE=2026-06-07 COUNT=5"
	@echo "  make collect OUTPUT_DIR=.var/local/raw-custom"
	@echo ""
	@echo "Preprocessing:"
	@echo "  make preprocess"
	@echo "  make preprocess DATE=2026-06-07"
	@echo "  make preprocess RAW_DIR=.var/local/raw PROCESSED_DIR=.var/local/processed"
	@echo "  make trace-collect"
	@echo "  make trace-preprocess"
	@echo "  make fetch-trace-history"
	@echo ""
	@echo "Quality:"
	@echo "  make test"
	@echo "  make test-unit"
	@echo "  make test-collection"
	@echo "  make lint"
	@echo "  make lint-fix"
	@echo "  make format"
	@echo "  make format-check"
	@echo "  make check"
	@echo "  make build"
	@echo "  make verify"
	@echo "  make quality"
	@echo "  make ci-quality"
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
	@echo "  TRACE_HISTORY_BRANCH Remote trace history branch. Default: tracing-history"
	@echo "  TRACE_HISTORY_DIR    Local trace history checkout. Default: .var/remote/tracing-history"
	@echo "  SERVICE     Optional service key. Default: all services"
	@echo "  DATE        Optional target date. Default: TODAYINTECH_TARGET_DATE or today"
	@echo "  COUNT       Optional preview article count. Default: collector CLI default"
	@echo "  OUTPUT_DIR    Optional raw output root. Default: TODAYINTECH_RAW_OUTPUT_DIR or .var/local/raw"
	@echo "  RAW_DIR       Optional preprocessing raw input root"
	@echo "  PROCESSED_DIR Optional preprocessing output root"
	@echo "  BRIEFED_STATE Optional briefed article state JSON path"
	@echo "  TRACE_DIR     Trace output root. Default: .var/local/traces"
	@echo "  REPORT_DIR    Test report output root. Default: .var/local/reports"
	@echo "  CI_RAW_DIR    GitHub Actions raw output root. Default: .artifacts/raw"
	@echo "  CI_PROCESSED_DIR GitHub Actions processed output root. Default: .artifacts/processed"
	@echo "  CI_TRACE_DIR  GitHub Actions trace output root. Default: .artifacts/traces"
	@echo "  CI_REPORT_DIR GitHub Actions report output root. Default: .artifacts/reports"

collect:
	$(PYTHON) -m src.collection $(COLLECT_ARGS)

preprocess:
	$(PYTHON) -m src.processing $(PREPROCESS_ARGS)

trace-collect:
	$(PYTHON) -m src.collection $(COLLECT_ARGS) --trace-dir $(TRACE_DIR)

trace-preprocess:
	$(PYTHON) -m src.processing $(PREPROCESS_ARGS) --trace-dir $(TRACE_DIR)

fetch-trace-history:
	mkdir -p $(dir $(TRACE_HISTORY_DIR))
	@if [ -d "$(TRACE_HISTORY_DIR)/.git" ]; then \
		git -C "$(TRACE_HISTORY_DIR)" fetch origin "$(TRACE_HISTORY_BRANCH)"; \
		git -C "$(TRACE_HISTORY_DIR)" checkout "$(TRACE_HISTORY_BRANCH)"; \
		git -C "$(TRACE_HISTORY_DIR)" pull --ff-only origin "$(TRACE_HISTORY_BRANCH)"; \
	else \
		git clone --branch "$(TRACE_HISTORY_BRANCH)" --single-branch \
			"$$(git remote get-url origin)" "$(TRACE_HISTORY_DIR)"; \
	fi

generate:
	$(PYTHON) -m src.main

test:
	mkdir -p $(REPORT_DIR)
	$(PYTHON) -m pytest tests --junitxml=$(REPORT_DIR)/junit.xml

test-unit:
	mkdir -p $(REPORT_DIR)
	$(PYTHON) -m pytest tests/unit --junitxml=$(REPORT_DIR)/unit.xml

test-collection:
	mkdir -p $(REPORT_DIR)
	$(PYTHON) -m pytest tests/collection --junitxml=$(REPORT_DIR)/collection.xml

lint:
	$(PYTHON) -m ruff check .

lint-fix:
	$(PYTHON) -m ruff check . --fix

format:
	$(PYTHON) -m ruff format .

format-check:
	$(PYTHON) -m ruff format --check .

check: lint format-check test

build:
	$(NPM) run build

verify: check build

quality: test trace-collect trace-preprocess

ci-quality:
	TODAYINTECH_RAW_OUTPUT_DIR=$(CI_RAW_DIR) $(MAKE) test REPORT_DIR=$(CI_REPORT_DIR)
	TODAYINTECH_RAW_OUTPUT_DIR=$(CI_RAW_DIR) $(MAKE) trace-collect OUTPUT_DIR=$(CI_RAW_DIR) TRACE_DIR=$(CI_TRACE_DIR)
	TODAYINTECH_RAW_OUTPUT_DIR=$(CI_RAW_DIR) $(MAKE) trace-preprocess RAW_DIR=$(CI_RAW_DIR) PROCESSED_DIR=$(CI_PROCESSED_DIR) TRACE_DIR=$(CI_TRACE_DIR)

ci: verify

deploy:
	$(GH) workflow run daily-briefing.yml $(WORKFLOW_ARGS)

deploy-status:
	$(GH) run list --workflow daily-briefing.yml --limit 5
