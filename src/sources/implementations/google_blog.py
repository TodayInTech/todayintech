from src.sources.contracts.base import BaseNewsSource
from src.sources.contracts.config import SourceConfig


class GoogleBlogSource(BaseNewsSource):
    service_key = "google-blog"
    service_name = "Google Blog"
    collector_type = "rss"
    source_url = "https://blog.google/technology/rss/"

    def source_config(self) -> SourceConfig:
        return {}
