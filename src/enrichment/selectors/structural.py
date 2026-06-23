import re
from dataclasses import dataclass

from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import BaseEvidenceSelector
from src.enrichment.models import EvidenceChunk

TOKEN_PATTERN = re.compile(r"[a-z0-9][a-z0-9_+.-]{2,}|[가-힣]{2,}", re.IGNORECASE)
STOPWORDS = {
    "about",
    "after",
    "also",
    "and",
    "are",
    "blog",
    "for",
    "from",
    "how",
    "into",
    "new",
    "news",
    "not",
    "our",
    "that",
    "the",
    "this",
    "with",
    "you",
    "대한",
    "에서",
    "으로",
    "있는",
    "한다",
    "하는",
}


@dataclass(frozen=True)
class ScoredChunk:
    chunk: EvidenceChunk
    score: float


class StructuralEvidenceSelector(BaseEvidenceSelector):
    name = "structural-keyword-position"

    def __init__(self, *, max_selected_tokens: int = 4000, min_chunks: int = 2) -> None:
        self.max_selected_tokens = max(max_selected_tokens, 1)
        self.min_chunks = max(min_chunks, 1)
        self.version = f"1:max={self.max_selected_tokens}:min_chunks={self.min_chunks}"

    def select(self, context: EnrichmentContext) -> list[EvidenceChunk]:
        chunks = context.chunks
        if not chunks:
            return []

        query_terms = self._query_terms(context)
        scored = [
            ScoredChunk(chunk=chunk, score=self._score_chunk(chunk, query_terms, len(chunks)))
            for chunk in chunks
        ]
        ranked = sorted(scored, key=lambda item: (-item.score, item.chunk.position))

        selected: list[EvidenceChunk] = []
        selected_tokens = 0
        for item in ranked:
            chunk = item.chunk
            if selected and selected_tokens + chunk.token_count > self.max_selected_tokens:
                continue
            selected.append(chunk)
            selected_tokens += chunk.token_count
            if selected_tokens >= self.max_selected_tokens:
                break

        selected = self._ensure_boundary_chunks(selected, chunks)
        if len(selected) < self.min_chunks:
            selected = self._fill_minimum_chunks(selected, chunks)

        return sorted(
            self._deduplicate_with_budget(selected),
            key=lambda chunk: chunk.position,
        )

    def _query_terms(self, context: EnrichmentContext) -> set[str]:
        article = context.candidate.article
        values = [
            article.title,
            context.candidate.feed_summary,
            " ".join(article.tags),
        ]
        return {
            token
            for value in values
            for token in TOKEN_PATTERN.findall(value.lower())
            if token not in STOPWORDS
        }

    def _score_chunk(
        self,
        chunk: EvidenceChunk,
        query_terms: set[str],
        total_chunks: int,
    ) -> float:
        chunk_terms = set(TOKEN_PATTERN.findall(chunk.text.lower()))
        score = len(query_terms & chunk_terms) * 4.0
        if chunk.heading_path:
            heading_terms = set(TOKEN_PATTERN.findall(" ".join(chunk.heading_path).lower()))
            score += len(query_terms & heading_terms) * 2.0
            score += 0.5
        if chunk.position == 0:
            score += 2.0
        if chunk.position == total_chunks - 1:
            score += 1.25
        if chunk.token_count >= 80:
            score += 0.5
        return score

    def _ensure_boundary_chunks(
        self,
        selected: list[EvidenceChunk],
        chunks: list[EvidenceChunk],
    ) -> list[EvidenceChunk]:
        selected_ids = {chunk.chunk_id for chunk in selected}
        with_boundaries = list(selected)
        for boundary in (chunks[0], chunks[-1]):
            if boundary.chunk_id not in selected_ids:
                with_boundaries.append(boundary)
                selected_ids.add(boundary.chunk_id)
        return with_boundaries

    def _fill_minimum_chunks(
        self,
        selected: list[EvidenceChunk],
        chunks: list[EvidenceChunk],
    ) -> list[EvidenceChunk]:
        selected_ids = {chunk.chunk_id for chunk in selected}
        filled = list(selected)
        for chunk in chunks:
            if chunk.chunk_id in selected_ids:
                continue
            filled.append(chunk)
            selected_ids.add(chunk.chunk_id)
            if len(filled) >= self.min_chunks:
                break
        return filled

    def _deduplicate_with_budget(self, chunks: list[EvidenceChunk]) -> list[EvidenceChunk]:
        selected: list[EvidenceChunk] = []
        selected_ids: set[str] = set()
        selected_tokens = 0
        for chunk in sorted(chunks, key=lambda item: item.position):
            if chunk.chunk_id in selected_ids:
                continue
            if selected and selected_tokens + chunk.token_count > self.max_selected_tokens:
                continue
            selected.append(chunk)
            selected_ids.add(chunk.chunk_id)
            selected_tokens += chunk.token_count
        return selected
