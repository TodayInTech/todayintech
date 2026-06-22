from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.enums import ExcludedReason
from src.processing.models import ArticleCandidate


class ValidationStep(BasePreprocessingStep):
    name = "validation"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        raw_count = 0
        for result in context.collection_results:
            raw_count += len(result.articles)
            if result.status == "failed":
                continue
            for article in result.articles:
                if not article.title.strip() or not str(article.url).strip():
                    context.increment_stat("invalid_removed")
                    context.increment_stat(f"excluded_reason:{ExcludedReason.INVALID_ARTICLE}")
                    continue
                context.add_candidate(
                    ArticleCandidate(
                        service_key=result.service_key,
                        service_name=result.service_name,
                        article=article,
                    )
                )
        context.stats["raw_count"] = raw_count
        return context
