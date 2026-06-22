from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.enums import ExcludedReason
from src.processing.models import ArticleCandidate


class RunDeduplicationStep(BasePreprocessingStep):
    name = "run_deduplication"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        seen_urls: set[str] = set()
        seen_titles: set[tuple[str, str]] = set()
        kept: list[ArticleCandidate] = []

        for candidate in context.candidates:
            title_key = (candidate.service_key, candidate.title_fingerprint)
            if candidate.normalized_url in seen_urls or title_key in seen_titles:
                context.exclude_candidate(candidate, ExcludedReason.DUPLICATE_IN_RUN)
                context.increment_stat("duplicate_removed")
                continue
            seen_urls.add(candidate.normalized_url)
            seen_titles.add(title_key)
            kept.append(candidate)

        context.replace_candidates(kept)
        return context
