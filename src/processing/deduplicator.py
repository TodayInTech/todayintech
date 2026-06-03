from src.models import Article


def deduplicate_articles(articles: list[Article]) -> list[Article]:
    seen_urls: set[str] = set()
    unique_articles: list[Article] = []

    for article in articles:
        url = str(article.url).rstrip("/")
        if url in seen_urls:
            continue
        seen_urls.add(url)
        unique_articles.append(article)

    return unique_articles
