from src.models import Article


def score_article(article: Article) -> tuple[int, str]:
    text = f"{article.title} {article.summary or ''}".lower()
    high_signal = ("release", "launch", "security", "model", "agent", "api", "open source")
    score = 4 if any(keyword in text for keyword in high_signal) else 3
    return score, "RSS 메타데이터 기반 MVP 휴리스틱 점수입니다."
