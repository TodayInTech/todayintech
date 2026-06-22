from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.enums import ExcludedReason
from src.processing.models import ArticleCandidate
from src.processing.state.briefed_article_store import BriefedArticleStore


class BriefedArticleFilterStep(BasePreprocessingStep):
    name = "briefed_article_filter"

    def __init__(self, store: BriefedArticleStore) -> None:
        self.store = store

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        kept: list[ArticleCandidate] = []
        for candidate in context.candidates:
            if self.store.contains(
                candidate.normalized_url,
                candidate.title_fingerprint,
                candidate.service_key,
                candidate.suggested_article_path,
            ):
                context.exclude_candidate(candidate, ExcludedReason.ALREADY_BRIEFED)
                context.increment_stat("already_briefed_removed")
                continue
            kept.append(candidate)
        context.replace_candidates(kept)
        return context
