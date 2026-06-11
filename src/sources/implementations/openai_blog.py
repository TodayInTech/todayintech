from src.sources.contracts.base import BaseNewsSource
from src.sources.contracts.config import SourceConfig


class OpenAIBlogSource(BaseNewsSource):
    service_key = "openai-blog"
    service_name = "OpenAI Blog"
    collector_type = "rss"
    source_url = "https://openai.com/news/rss.xml"

    def source_config(self) -> SourceConfig:
        return {
            "collection_limit": 50,
            "lookback_days": 90,
        }
