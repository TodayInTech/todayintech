from src.sources.contracts.base import BaseNewsSource
from src.sources.contracts.config import SourceConfig


class AnthropicBlogSource(BaseNewsSource):
    service_key = "anthropic-blog"
    service_name = "Anthropic Blog"
    collector_type = "sitemap"
    source_url = "https://www.anthropic.com/sitemap.xml"

    def source_config(self) -> SourceConfig:
        return {
            "url_prefixes": ("/news/",),
            "collection_limit": 20,
        }
