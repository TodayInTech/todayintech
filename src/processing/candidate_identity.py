import hashlib
import re
from datetime import UTC, datetime

from src.models import Article


def url_hash(normalized_url: str) -> str:
    return hashlib.sha256(normalized_url.encode("utf-8")).hexdigest()


def candidate_id(service_key: str, normalized_url: str) -> str:
    return f"{service_key}:{url_hash(normalized_url)[:16]}"


def suggested_doc_key(article: Article, normalized_url: str) -> str:
    published_at = article.published_at or article.collected_at or datetime.now(UTC)
    if published_at.tzinfo is None:
        published_at = published_at.replace(tzinfo=UTC)

    date_prefix = published_at.strftime("%Y-%m")
    title_slug = slugify_title(article.title)
    short_hash = url_hash(normalized_url)[:8]
    return f"{date_prefix}-{title_slug}-{short_hash}"


def suggested_article_path(service_key: str, doc_key: str) -> str:
    return f"docs/services/{service_key}/{doc_key}.md"


def slugify_title(value: str, fallback: str = "article") -> str:
    normalized = value.lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = re.sub(r"-+", "-", normalized).strip("-")
    return normalized[:72].strip("-") or fallback
