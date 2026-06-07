from src.sources.contracts.base import BaseNewsSource
from src.sources.contracts.config import SourceConfig


class GitHubBlogSource(BaseNewsSource):
    service_key = "github-blog"
    service_name = "GitHub Blog"
    collector_type = "rss"
    source_url = "https://github.blog/feed/"

    def source_config(self) -> SourceConfig:
        return {}
