from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter

from src.enrichment.chunking import StructuralContentChunker
from src.enrichment.context import EnrichmentContext
from src.enrichment.contracts import (
    BaseContentChunker,
    BaseContentExtractor,
    BaseEnrichmentCache,
    BaseEnrichmentPolicy,
    BaseEnrichmentStep,
    BaseEvidenceSelector,
)
from src.enrichment.factories import (
    ContentExtractorFactory,
    ContentFetcherFactory,
    EnrichmentPipelineFactory,
)
from src.enrichment.models import (
    DocumentBlockType,
    EnrichedArticleCandidate,
    EnrichmentFailureReason,
    EnrichmentInputStrategy,
    EnrichmentRecord,
    EnrichmentResult,
    EnrichmentStatus,
)
from src.enrichment.policies import AdaptiveEnrichmentPolicy
from src.enrichment.selectors import StructuralEvidenceSelector
from src.enrichment.state import JsonEnrichmentCache
from src.enrichment.tokenization import TiktokenTokenCounter
from src.processing.models import ArticleCandidate, PreprocessingResult
from src.progress import log_info


class ContentEnricher:
    def __init__(
        self,
        *,
        steps: list[BaseEnrichmentStep],
        cache: BaseEnrichmentCache,
        extractor: BaseContentExtractor,
        chunker: BaseContentChunker,
        policy: BaseEnrichmentPolicy,
        selector: BaseEvidenceSelector,
    ) -> None:
        self.steps = steps
        self.cache = cache
        self.extractor = extractor
        self.chunker = chunker
        self.policy = policy
        self.selector = selector

    @classmethod
    def create_default(
        cls,
        *,
        cache_dir: Path,
        timeout_seconds: float,
        max_attempts: int,
        minimum_tokens: int,
        full_content_max_tokens: int,
        chunk_selection_max_tokens: int,
        chunk_max_tokens: int,
        selected_chunks_max_tokens: int,
    ) -> ContentEnricher:
        token_counter = TiktokenTokenCounter()
        extractor = ContentExtractorFactory().create(
            "text/html",
            token_counter=token_counter,
        )
        fetcher = ContentFetcherFactory().create_http(
            timeout_seconds=timeout_seconds,
            max_attempts=max_attempts,
        )
        policy = AdaptiveEnrichmentPolicy(
            minimum_tokens=minimum_tokens,
            full_content_max_tokens=full_content_max_tokens,
            chunk_selection_max_tokens=chunk_selection_max_tokens,
        )
        chunker = StructuralContentChunker(chunk_max_tokens)
        selector = StructuralEvidenceSelector(max_selected_tokens=selected_chunks_max_tokens)
        steps = EnrichmentPipelineFactory().create_default(
            fetcher=fetcher,
            extractor=extractor,
            chunker=chunker,
            policy=policy,
            selector=selector,
        )
        return cls(
            steps=steps,
            cache=JsonEnrichmentCache(cache_dir),
            extractor=extractor,
            chunker=chunker,
            policy=policy,
            selector=selector,
        )

    def enrich(self, preprocessing_result: PreprocessingResult) -> EnrichmentResult:
        started_at = perf_counter()
        candidates = [
            candidate
            for service in preprocessing_result.services
            for candidate in service.candidates
        ]
        records: list[EnrichmentRecord] = []
        enriched_candidates: list[EnrichedArticleCandidate] = []
        log_info("Enrichment", f"후보 원문 보강 시작: candidates={len(candidates)}")

        for index, candidate in enumerate(candidates, start=1):
            cache_key = self.cache.build_key(
                candidate,
                extractor_name=self.extractor.name,
                extractor_version=self.extractor.version,
                chunker_name=self.chunker.name,
                policy_name=self.policy.name,
                policy_version=self.policy.version,
                selector_name=self.selector.name,
                selector_version=self.selector.version,
            )
            cached = self.cache.get(cache_key)
            if cached is not None:
                cached = cached.model_copy(update={"candidate": candidate})
                record = _record_from_result(cached, cache_hit=True)
                records.append(record)
                enriched_candidates.append(cached)
                log_info(
                    "Enrichment",
                    f"({index}/{len(candidates)}) cache hit: {candidate.article.title}",
                )
                continue

            context = EnrichmentContext(
                candidate=candidate,
                record=_initial_record(candidate),
            )
            for step in self.steps:
                context = step.process(context)

            if context.result is None:
                context.fail(
                    reason=EnrichmentFailureReason.UNKNOWN,
                    detail="Enrichment pipeline completed without a result",
                    allow_fallback=False,
                )
            assert context.result is not None
            _sync_record(context.record, context.result)
            records.append(context.record)
            enriched_candidates.append(context.result)
            if context.result.status == EnrichmentStatus.ENRICHED:
                self.cache.save(cache_key, context.result)
            log_info(
                "Enrichment",
                (
                    f"({index}/{len(candidates)}) 완료: "
                    f"status={context.result.status.value}, "
                    f"strategy={context.result.input_strategy.value}"
                ),
            )

        return EnrichmentResult(
            generated_for=preprocessing_result.generated_for,
            generated_at=datetime.now(UTC),
            duration_ms=round((perf_counter() - started_at) * 1000),
            policy_name=self.policy.name,
            policy_version=self.policy.version,
            records=records,
            candidates=enriched_candidates,
            archived_articles=preprocessing_result.archived_articles,
            service_names={
                service.service_key: service.service_name
                for service in preprocessing_result.services
            },
        )


def _initial_record(candidate: ArticleCandidate) -> EnrichmentRecord:
    return EnrichmentRecord(
        candidate_id=candidate.candidate_id,
        service_key=candidate.service_key,
        service_name=candidate.service_name,
        title=candidate.article.title,
        source_url=candidate.normalized_url,
        status=EnrichmentStatus.FAILED,
        input_strategy=EnrichmentInputStrategy.NONE,
    )


def _record_from_result(
    result: EnrichedArticleCandidate,
    *,
    cache_hit: bool,
) -> EnrichmentRecord:
    record = _initial_record(result.candidate)
    record.cache_hit = cache_hit
    document = result.document
    if document is not None:
        record.content_hash = document.content_hash
        record.document_type = document.document_type
        record.detected_language = document.detected_language
        record.extracted_char_count = document.char_count
        record.extracted_token_count = document.token_count
        record.section_count = sum(
            block.block_type == DocumentBlockType.HEADING for block in document.blocks
        )
        record.code_block_count = sum(
            block.block_type == DocumentBlockType.CODE for block in document.blocks
        )
        record.table_count = sum(
            block.block_type == DocumentBlockType.TABLE for block in document.blocks
        )
        record.list_item_count = sum(
            block.block_type == DocumentBlockType.LIST_ITEM for block in document.blocks
        )
    record.chunk_count = len(result.chunks)
    _sync_record(record, result)
    return record


def _sync_record(
    record: EnrichmentRecord,
    result: EnrichedArticleCandidate,
) -> None:
    record.status = result.status
    record.input_strategy = result.input_strategy
    record.input_strategy_reason = result.input_strategy_reason
    record.selected_chunk_count = len(result.selected_chunks)
    record.selected_token_count = sum(chunk.token_count for chunk in result.selected_chunks)
    record.failure_reason = result.failure_reason
    record.failure_detail = result.failure_detail
