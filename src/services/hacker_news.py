from src.services.rss_service import RssNewsService


class HackerNewsService(RssNewsService):
    service_key = "hacker-news"
    service_name = "Hacker News"
    feed_url = "https://hnrss.org/frontpage"
