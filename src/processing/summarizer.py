from src.models import Article, ArticleSummary
from src.processing.classifier import classify_article
from src.processing.scorer import score_article


def summarize_article(article: Article) -> ArticleSummary:
    score, reason = score_article(article)
    source_summary = article.summary or "RSS 피드에 요약이 제공되지 않았습니다."
    return ArticleSummary(
        article=article,
        category=classify_article(article),
        importance_score=score,
        importance_reason=reason,
        summary_ko=source_summary,
        why_it_matters_ko="MVP 단계에서는 RSS 메타데이터를 기반으로 중요도를 판단합니다.",
    )
