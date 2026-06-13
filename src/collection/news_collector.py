from datetime import UTC, datetime
from time import perf_counter

from src.collection.factories.collector_strategy_factory import CollectorStrategyFactory
from src.models import ServiceCollectionResult
from src.progress import log_info
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
        sources = self.source_factory.create_all()
        results: list[ServiceCollectionResult] = []
        for index, source in enumerate(sources, start=1):
            log_info(
                "Collector",
                f"({index}/{len(sources)}) {source.service_key} 수집 시작: {source.collector_type}",
            )
            result = self.collect_source(source)
            log_info(
                "Collector",
                (
                    f"({index}/{len(sources)}) {source.service_key} {result.status}: "
                    f"articles={len(result.articles)}, duration_ms={result.duration_ms}"
                ),
            )
            results.append(result)
        return results

    def collect_by_service_key(self, service_key: str) -> ServiceCollectionResult:
        source = self.source_factory.create(service_key)
        return self.collect_source(source)

    def collect_source(self, source: BaseNewsSource) -> ServiceCollectionResult:
        collected_at = datetime.now(UTC)
        started_at = perf_counter()
        try:
            strategy = self.strategy_factory.create(source.collector_type)
            articles = strategy.collect(source)
        except Exception as exc:
            duration_ms = int((perf_counter() - started_at) * 1000)
            return ServiceCollectionResult(
                service_key=source.service_key,
                service_name=source.service_name,
                source_url=source.source_url,
                collection_method=source.collector_type,
                collected_at=collected_at,
                status="failed",
                duration_ms=duration_ms,
                error=str(exc),
            )

        duration_ms = int((perf_counter() - started_at) * 1000)
        warning_codes = []
        if not articles:
            warning_codes.append("empty_collection")

        return ServiceCollectionResult(
            service_key=source.service_key,
            service_name=source.service_name,
            source_url=source.source_url,
            collection_method=source.collector_type,
            collected_at=collected_at,
            status="success",
            duration_ms=duration_ms,
            articles=articles,
            warning_codes=warning_codes,
        )
