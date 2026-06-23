from pathlib import Path

from src.settings import AppSettings, parse_dotenv_line


def test_settings_from_env_uses_defaults(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("TODAYINTECH_WRITER_AGENT", raising=False)
    monkeypatch.delenv("TODAYINTECH_MAX_ARTICLES_PER_SERVICE", raising=False)
    monkeypatch.delenv("TODAYINTECH_TRACE_OUTPUT_DIR", raising=False)
    monkeypatch.delenv("TODAYINTECH_ENRICHED_OUTPUT_DIR", raising=False)
    monkeypatch.delenv("TODAYINTECH_ENRICHMENT_CACHE_DIR", raising=False)

    settings = AppSettings.from_env()

    assert settings.openai_api_key is None
    assert settings.writer_agent == "draft"
    assert settings.max_articles_per_service == 5
    assert settings.trace_output_dir == Path(".var/local/traces")
    assert settings.enriched_output_dir == Path(".var/local/enriched")
    assert settings.enrichment_cache_dir == Path(".var/local/enrichment-cache")
    assert settings.enrichment_full_content_max_tokens == 4000
    assert settings.enrichment_chunk_selection_max_tokens == 8000


def test_settings_resolve_target_date_prefers_override(monkeypatch) -> None:
    monkeypatch.setenv("TODAYINTECH_TARGET_DATE", "2026-06-01")

    settings = AppSettings.from_env()

    assert settings.resolve_target_date("2026-06-07") == "2026-06-07"


def test_settings_minimum_article_count(monkeypatch) -> None:
    monkeypatch.setenv("TODAYINTECH_MAX_ARTICLES_PER_SERVICE", "0")

    settings = AppSettings.from_env()

    assert settings.max_articles_per_service == 1


def test_settings_writer_agent_can_be_overridden(monkeypatch) -> None:
    monkeypatch.setenv("TODAYINTECH_WRITER_AGENT", "OpenAI")

    settings = AppSettings.from_env()

    assert settings.writer_agent == "openai"
    assert settings.with_writer_agent("draft").writer_agent == "draft"


def test_settings_loads_dotenv_from_current_directory(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("TODAYINTECH_WRITER_AGENT", raising=False)
    tmp_path.joinpath(".env").write_text(
        "OPENAI_API_KEY=sk-test\nTODAYINTECH_WRITER_AGENT=openai\n",
        encoding="utf-8",
    )

    settings = AppSettings.from_env()

    assert settings.openai_api_key == "sk-test"
    assert settings.writer_agent == "openai"


def test_settings_dotenv_does_not_override_existing_environment(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY", "sk-from-shell")
    tmp_path.joinpath(".env").write_text("OPENAI_API_KEY=sk-from-file\n", encoding="utf-8")

    settings = AppSettings.from_env()

    assert settings.openai_api_key == "sk-from-shell"


def test_parse_dotenv_line_handles_comments_and_quotes() -> None:
    assert parse_dotenv_line("# comment") == (None, "")
    assert parse_dotenv_line("OPENAI_API_KEY='sk-test'") == ("OPENAI_API_KEY", "sk-test")
