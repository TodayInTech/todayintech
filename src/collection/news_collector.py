from datetime import UTC, datetime

from src.collection.factories.collector_strategy_factory import CollectorStrategyFactory
from src.models import ServiceCollectionResult
from src.sources import NewsSourceFactory
from src.sources.contracts.base import BaseNewsSource


class NewsCollector:
    """Collect articles from all registered news sources."""

    def __init__(
        self,
        source_factory: NewsSourceFactory | None = None,
        strategy_factory: CollectorStrategyFactory | None = None,
    ) -> None:
        self.source_factory = source_factory or NewsSourceFactory()
        self.strategy_factory = strategy_factory or CollectorStrategyFactory()

    def collect_all(self) -> list[ServiceCollectionResult]:
        return [self.collect_source(source) for source in self.source_factory.create_all()]

    def collect_by_service_key(self, service_key: str) -> ServiceCollectionResult:
        source = self.source_factory.create(service_key)
        return self.collect_source(source)

    def collect_source(self, source: BaseNewsSource) -> ServiceCollectionResult:
        collected_at = datetime.now(UTC)
        try:
            strategy = self.strategy_factory.create(source.collector_type)
            articles = strategy.collect(source)
        except Exception as exc:
            return ServiceCollectionResult(
                service_key=source.service_key,
                service_name=source.service_name,
                source_url=source.source_url,
                collection_method=source.collector_type,
                collected_at=collected_at,
                status="failed",
                error=str(exc),
            )

        return ServiceCollectionResult(
            service_key=source.service_key,
            service_name=source.service_name,
            source_url=source.source_url,
            collection_method=source.collector_type,
            collected_at=collected_at,
            status="success",
            articles=articles,
        )
