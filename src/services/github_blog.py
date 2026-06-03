from src.services.rss_service import RssNewsService


class GitHubBlogService(RssNewsService):
    service_key = "github-blog"
    service_name = "GitHub Blog"
    feed_url = "https://github.blog/feed/"
