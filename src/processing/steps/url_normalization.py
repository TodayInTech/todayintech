from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.identity.url_normalizer import normalize_url, title_fingerprint


class UrlNormalizationStep(BasePreprocessingStep):
    name = "url_normalization"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        context.replace_candidates(
            [
                candidate.model_copy(
                    update={
                        "normalized_url": normalize_url(str(candidate.article.url)),
                        "title_fingerprint": title_fingerprint(candidate.article.title),
                    }
                )
                for candidate in context.candidates
            ]
        )
        return context
