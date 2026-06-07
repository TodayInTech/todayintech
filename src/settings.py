import os
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


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


@dataclass(frozen=True)
class AppSettings:
    openai_api_key: str | None
    openai_model: str
    timezone: str
    output_dir: Path
    raw_output_dir: Path
    max_articles_per_service: int
    target_date: str | None
    docusaurus_url: str
    docusaurus_base_url: str

    @classmethod
    def from_env(cls) -> AppSettings:
        return cls(
            openai_api_key=_optional_env("OPENAI_API_KEY"),
            openai_model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
            timezone=os.getenv("TODAYINTECH_TIMEZONE", "Asia/Seoul"),
            output_dir=Path(os.getenv("TODAYINTECH_OUTPUT_DIR", "docs")),
            raw_output_dir=Path(os.getenv("TODAYINTECH_RAW_OUTPUT_DIR", "data/raw")),
            max_articles_per_service=_int_env(
                "TODAYINTECH_MAX_ARTICLES_PER_SERVICE",
                default=5,
                minimum=1,
            ),
            target_date=_optional_env("TODAYINTECH_TARGET_DATE"),
            docusaurus_url=os.getenv("DOCUSAURUS_URL", "https://example.com"),
            docusaurus_base_url=os.getenv("DOCUSAURUS_BASE_URL", "/"),
        )

    def resolve_target_date(self, override: str | None = None) -> str:
        return override or self.target_date or datetime.now(UTC).date().isoformat()


SETTINGS = AppSettings.from_env()
