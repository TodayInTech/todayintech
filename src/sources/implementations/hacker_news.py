from src.sources.contracts.base import BaseNewsSource
from src.sources.contracts.config import SourceConfig


class HackerNewsSource(BaseNewsSource):
    service_key = "hacker-news"
    service_name = "Hacker News"
    collector_type = "rss"
    source_url = "https://hnrss.org/frontpage"

    def source_config(self) -> SourceConfig:
        return {}
