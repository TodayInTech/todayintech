from src.processing.context import PreprocessingContext
from src.processing.contracts import BasePreprocessingStep
from src.processing.identity.candidate_identity import (
    candidate_id,
    suggested_article_path,
    suggested_doc_key,
    url_hash,
)


class CandidateIdentityStep(BasePreprocessingStep):
    name = "candidate_identity"

    def process(self, context: PreprocessingContext) -> PreprocessingContext:
        updated_candidates = []
        for candidate in context.candidates:
            candidate_url_hash = url_hash(candidate.normalized_url)
            doc_key = suggested_doc_key(candidate.article, candidate.normalized_url)
            updated_candidates.append(
                candidate.model_copy(
                    update={
                        "candidate_id": candidate_id(
                            candidate.service_key,
                            candidate.normalized_url,
                        ),
                        "url_hash": candidate_url_hash,
                        "feed_summary": candidate.article.summary or "",
                        "suggested_doc_key": doc_key,
                        "suggested_article_path": suggested_article_path(
                            candidate.service_key,
                            doc_key,
                        ),
                    }
                )
            )

        context.replace_candidates(updated_candidates)
        return context
