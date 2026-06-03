from src.services.rss_service import RssNewsService


class AnthropicBlogService(RssNewsService):
    service_key = "anthropic-blog"
    service_name = "Anthropic Blog"
    feed_url = "https://www.anthropic.com/news/rss.xml"
