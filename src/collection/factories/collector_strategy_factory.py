from src.collection.strategies.base import BaseCollectorStrategy
from src.collection.strategies.rss import RssCollector
from src.collection.strategies.sitemap import SitemapCollector


class CollectorStrategyFactory:
    _registry: dict[str, type[BaseCollectorStrategy]] = {
        RssCollector.collector_type: RssCollector,
        SitemapCollector.collector_type: SitemapCollector,
    }

    def create(self, collector_type: str) -> BaseCollectorStrategy:
        try:
            collector_class = self._registry[collector_type]
        except KeyError as exc:
            available = ", ".join(sorted(self._registry))
            raise ValueError(
                f"Unknown collector type '{collector_type}'. Available: {available}"
            ) from exc
        return collector_class()
