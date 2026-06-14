from datetime import UTC, datetime
from pathlib import Path

from src import main as pipeline_main
from src.models import Article, ServiceCollectionResult


class FakeSettings:
    openai_api_key = None
    openai_model = "gpt-5-mini"
    writer_agent = "draft"
    max_candidates_per_service = 10
    max_candidates_total = 50

    def __init__(self, root: Path) -> None:
        self.output_dir = root / "docs"
        self.raw_output_dir = root / "raw"
        self.processed_output_dir = root / "processed"
        self.briefed_articles_path = root / "data" / "briefed_articles.json"

    def resolve_target_date(self, override: str | None = None) -> str:
        return override or "2026-06-11"


class FakeCollector:
    def __init__(self, _source_factory) -> None:
        pass

    def collect_all(self) -> list[ServiceCollectionResult]:
        return [
            ServiceCollectionResult(
                service_key="hacker-news",
                service_name="Hacker News",
                source_url="https://hnrss.org/frontpage",
                collection_method="rss",
                collected_at=datetime(2026, 6, 11, tzinfo=UTC),
                status="success",
                duration_ms=1,
                articles=[
                    Article(
                        source="Hacker News",
                        title="New Agent Release",
                        url="https://example.com/agent?utm_source=hn",
                        published_at=datetime(2026, 6, 10, tzinfo=UTC),
                        collected_at=datetime(2026, 6, 11, tzinfo=UTC),
                        summary="Agent release",
                    )
                ],
            )
        ]


class FakeSourceFactory:
    pass


def test_run_pipeline_writes_raw_and_preprocessed_outputs(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(pipeline_main, "SETTINGS", FakeSettings(tmp_path))
    monkeypatch.setattr(pipeline_main, "NewsCollector", FakeCollector)
    monkeypatch.setattr(pipeline_main, "NewsSourceFactory", FakeSourceFactory)

    result = pipeline_main.run_pipeline("2026-06-11")

    assert result.generated_for == "2026-06-11"
    assert tmp_path.joinpath("raw", "2026-06-11", "summary.json").exists()
    assert tmp_path.joinpath("processed", "2026-06-11", "preprocessing.json").exists()
    assert tmp_path.joinpath("docs", "index.md").exists()
    assert tmp_path.joinpath("docs", "services", "hacker-news.md").exists()
    assert list(tmp_path.joinpath("docs", "services", "hacker-news").glob("*.md"))
    assert tmp_path.joinpath("data", "briefed_articles.json").exists()
    assert result.editorial_result.services[0].briefings[0].title == "New Agent Release"
