from pathlib import Path

from src.settings import AppSettings


def test_settings_from_env_uses_defaults(monkeypatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("TODAYINTECH_MAX_ARTICLES_PER_SERVICE", raising=False)
    monkeypatch.delenv("TODAYINTECH_TRACE_OUTPUT_DIR", raising=False)

    settings = AppSettings.from_env()

    assert settings.openai_api_key is None
    assert settings.max_articles_per_service == 5
    assert settings.trace_output_dir == Path("data/traces")


def test_settings_resolve_target_date_prefers_override(monkeypatch) -> None:
    monkeypatch.setenv("TODAYINTECH_TARGET_DATE", "2026-06-01")

    settings = AppSettings.from_env()

    assert settings.resolve_target_date("2026-06-07") == "2026-06-07"


def test_settings_minimum_article_count(monkeypatch) -> None:
    monkeypatch.setenv("TODAYINTECH_MAX_ARTICLES_PER_SERVICE", "0")

    settings = AppSettings.from_env()

    assert settings.max_articles_per_service == 1
