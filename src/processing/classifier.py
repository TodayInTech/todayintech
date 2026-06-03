from src.models import Article, NewsCategory


def classify_article(article: Article) -> NewsCategory:
    text = f"{article.title} {article.summary or ''}".lower()
    if any(keyword in text for keyword in ("ai", "openai", "anthropic", "model", "llm")):
        return NewsCategory.AI
    if any(keyword in text for keyword in ("cloud", "aws", "gcp", "infrastructure")):
        return NewsCategory.CLOUD
    if any(keyword in text for keyword in ("github", "developer", "api", "sdk")):
        return NewsCategory.DEVELOPER_TOOLS
    if any(keyword in text for keyword in ("security", "vulnerability", "cve")):
        return NewsCategory.SECURITY
    return NewsCategory.OTHER
