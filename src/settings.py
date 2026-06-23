import os
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from pathlib import Path

ENV_FILE_PATH = Path(".env")


def load_dotenv(path: Path = ENV_FILE_PATH) -> None:
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        key, value = parse_dotenv_line(line)
        if key and key not in os.environ:
            os.environ[key] = value


def parse_dotenv_line(line: str) -> tuple[str | None, str]:
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or "=" not in stripped:
        return None, ""

    key, value = stripped.split("=", 1)
    key = key.strip()
    value = value.strip()
    if not key:
        return None, ""

    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return key, value


def _optional_env(name: str) -> str | None:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return None
    return value


def _int_env(name: str, default: int, minimum: int | None = None) -> int:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return default

    try:
        parsed = int(value)
    except ValueError:
        return default

    if minimum is not None:
        return max(minimum, parsed)
    return parsed


def _float_env(name: str, default: float, minimum: float | None = None) -> float:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return default
    try:
        parsed = float(value)
    except ValueError:
        return default
    return max(minimum, parsed) if minimum is not None else parsed


@dataclass(frozen=True)
class AppSettings:
    openai_api_key: str | None
    openai_model: str
    writer_agent: str
    timezone: str
    output_dir: Path
    raw_output_dir: Path
    processed_output_dir: Path
    enriched_output_dir: Path
    enrichment_cache_dir: Path
    trace_output_dir: Path
    briefed_articles_path: Path
    max_articles_per_service: int
    max_candidates_per_service: int
    max_candidates_total: int
    enrichment_timeout_seconds: float
    enrichment_max_attempts: int
    enrichment_minimum_tokens: int
    enrichment_full_content_max_tokens: int
    enrichment_chunk_selection_max_tokens: int
    enrichment_chunk_max_tokens: int
    target_date: str | None
    docusaurus_url: str
    docusaurus_base_url: str

    @classmethod
    def from_env(cls) -> AppSettings:
        load_dotenv()
        return cls(
            openai_api_key=_optional_env("OPENAI_API_KEY"),
            openai_model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
            writer_agent=os.getenv("TODAYINTECH_WRITER_AGENT", "draft").strip().lower() or "draft",
            timezone=os.getenv("TODAYINTECH_TIMEZONE", "Asia/Seoul"),
            output_dir=Path(os.getenv("TODAYINTECH_OUTPUT_DIR", "docs")),
            raw_output_dir=Path(os.getenv("TODAYINTECH_RAW_OUTPUT_DIR", ".var/local/raw")),
            processed_output_dir=Path(
                os.getenv("TODAYINTECH_PROCESSED_OUTPUT_DIR", ".var/local/processed")
            ),
            enriched_output_dir=Path(
                os.getenv("TODAYINTECH_ENRICHED_OUTPUT_DIR", ".var/local/enriched")
            ),
            enrichment_cache_dir=Path(
                os.getenv("TODAYINTECH_ENRICHMENT_CACHE_DIR", ".var/local/enrichment-cache")
            ),
            trace_output_dir=Path(os.getenv("TODAYINTECH_TRACE_OUTPUT_DIR", ".var/local/traces")),
            briefed_articles_path=Path(
                os.getenv("TODAYINTECH_BRIEFED_ARTICLES_PATH", "data/briefed_articles.json")
            ),
            max_articles_per_service=_int_env(
                "TODAYINTECH_MAX_ARTICLES_PER_SERVICE",
                default=5,
                minimum=1,
            ),
            max_candidates_per_service=_int_env(
                "TODAYINTECH_MAX_CANDIDATES_PER_SERVICE",
                default=10,
                minimum=1,
            ),
            max_candidates_total=_int_env(
                "TODAYINTECH_MAX_CANDIDATES_TOTAL",
                default=50,
                minimum=1,
            ),
            enrichment_timeout_seconds=_float_env(
                "TODAYINTECH_ENRICHMENT_TIMEOUT_SECONDS",
                default=20,
                minimum=1,
            ),
            enrichment_max_attempts=_int_env(
                "TODAYINTECH_ENRICHMENT_MAX_ATTEMPTS",
                default=2,
                minimum=1,
            ),
            enrichment_minimum_tokens=_int_env(
                "TODAYINTECH_ENRICHMENT_MINIMUM_TOKENS",
                default=100,
                minimum=1,
            ),
            enrichment_full_content_max_tokens=_int_env(
                "TODAYINTECH_ENRICHMENT_FULL_CONTENT_MAX_TOKENS",
                default=4000,
                minimum=1,
            ),
            enrichment_chunk_selection_max_tokens=_int_env(
                "TODAYINTECH_ENRICHMENT_CHUNK_SELECTION_MAX_TOKENS",
                default=8000,
                minimum=1,
            ),
            enrichment_chunk_max_tokens=_int_env(
                "TODAYINTECH_ENRICHMENT_CHUNK_MAX_TOKENS",
                default=1200,
                minimum=1,
            ),
            target_date=_optional_env("TODAYINTECH_TARGET_DATE"),
            docusaurus_url=os.getenv("DOCUSAURUS_URL", "https://example.com"),
            docusaurus_base_url=os.getenv("DOCUSAURUS_BASE_URL", "/"),
        )

    def resolve_target_date(self, override: str | None = None) -> str:
        return override or self.target_date or datetime.now(UTC).date().isoformat()

    def with_writer_agent(self, writer_agent: str) -> AppSettings:
        return replace(self, writer_agent=writer_agent.strip().lower())


SETTINGS = AppSettings.from_env()
