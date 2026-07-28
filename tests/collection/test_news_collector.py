from datetime import UTC, datetime

from src.collection.news_collector import NewsCollector
from src.collection.strategies.base import BaseCollectorStrategy
from src.models import Article
from src.sources.contracts.base import BaseNewsSource
from src.sources.contracts.config import SourceConfig


class FakeSource(BaseNewsSource):
    service_key = "fake-source"
    service_name = "Fake Source"
    collector_type = "fake"
    source_url = "https://example.com/sitemap.xml"

    def source_config(self) -> SourceConfig:
        return {}


class FakeSourceFactory:
    def create(self, _service_key: str) -> BaseNewsSource:
        return FakeSource()

    def create_all(self) -> list[BaseNewsSource]:
        return [FakeSource()]


class WarningStrategy(BaseCollectorStrategy):
    collector_type = "fake"

    def collect(self, source: BaseNewsSource) -> list[Article]:
        self.warning_codes = ["article_metadata_fetch_failed"]
        return [
            Article(
                source=source.service_name,
                title="Valid article",
                url="https://example.com/article",
                collected_at=datetime.now(UTC),
            )
        ]


class WarningStrategyFactory:
    def create(self, _collector_type: str) -> BaseCollectorStrategy:
        return WarningStrategy()


def test_news_collector_marks_strategy_warnings_as_partial() -> None:
    collector = NewsCollector(
        source_factory=FakeSourceFactory(),
        strategy_factory=WarningStrategyFactory(),
    )

    result = collector.collect_by_service_key("fake-source")

    assert result.status == "partial"
    assert result.warning_codes == ["article_metadata_fetch_failed"]
    assert len(result.articles) == 1
