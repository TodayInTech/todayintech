from src.services.rss_service import RssNewsService


class GoogleBlogService(RssNewsService):
    service_key = "google-blog"
    service_name = "Google Blog"
    feed_url = "https://blog.google/technology/rss/"
