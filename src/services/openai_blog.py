from src.services.rss_service import RssNewsService


class OpenAIBlogService(RssNewsService):
    service_key = "openai-blog"
    service_name = "OpenAI Blog"
    feed_url = "https://openai.com/news/rss.xml"
