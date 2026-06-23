from datetime import UTC, datetime

from src.enrichment.chunking import StructuralContentChunker
from src.enrichment.content_enricher import ContentEnricher
from src.enrichment.extractors import HtmlContentExtractor
from src.enrichment.factories import EnrichmentPipelineFactory
from src.enrichment.fetchers import HttpContentFetcher
from src.enrichment.models import EnrichmentInputStrategy, EnrichmentStatus
from src.enrichment.policies import AdaptiveEnrichmentPolicy
from src.enrichment.state import JsonEnrichmentCache
from src.enrichment.tokenization import TiktokenTokenCounter
from src.models import Article
from src.processing.models import (
    ArticleCandidate,
    PreprocessingResult,
    ServicePreprocessingResult,
)


class FakeFetcher(HttpContentFetcher):
    def __init__(self) -> None:
        self.calls = 0

    def fetch(self, url: str):
        from src.enrichment.models import FetchedContent

        self.calls += 1
        body = """
        <html><head><title>Agent Architecture</title></head>
        <body><article><h1>Agent Architecture</h1>
        <p>This article explains how a pipeline separates fetching, extraction,
        validation, chunking, and policy selection for reliable agent inputs.</p>
        <p>The design preserves source evidence and keeps operational traces measurable.</p>
        </article></body></html>
        """
        return FetchedContent(
            source_url=url,
            final_url=url,
            http_status=200,
            content_type="text/html",
            body=body,
            response_bytes=len(body.encode()),
            duration_ms=5,
        )


def make_preprocessing_result() -> PreprocessingResult:
    candidate = ArticleCandidate(
        candidate_id="openai-blog:abc",
        service_key="openai-blog",
        service_name="OpenAI Blog",
        normalized_url="https://openai.com/index/agent",
        article=Article(
            source="OpenAI Blog",
            title="Agent Architecture",
            url="https://openai.com/index/agent",
            collected_at=datetime(2026, 6, 23, tzinfo=UTC),
            summary="A detailed overview of a reliable agent pipeline architecture.",
        ),
        feed_summary="A detailed overview of a reliable agent pipeline architecture.",
    )
    return PreprocessingResult(
        generated_for="2026-06-23",
        generated_at=datetime(2026, 6, 23, tzinfo=UTC),
        raw_count=1,
        candidate_count=1,
        excluded_count=0,
        services=[
            ServicePreprocessingResult(
                service_key="openai-blog",
                service_name="OpenAI Blog",
                raw_count=1,
                candidate_count=1,
                excluded_count=0,
                candidates=[candidate],
            )
        ],
    )


def test_content_enricher_runs_pipeline_and_reuses_cache(tmp_path) -> None:
    fetcher = FakeFetcher()
    token_counter = TiktokenTokenCounter()
    extractor = HtmlContentExtractor(token_counter)
    policy = AdaptiveEnrichmentPolicy(minimum_tokens=10)
    chunker = StructuralContentChunker()
    steps = EnrichmentPipelineFactory().create_default(
        fetcher=fetcher,
        extractor=extractor,
        chunker=chunker,
        policy=policy,
    )
    enricher = ContentEnricher(
        steps=steps,
        cache=JsonEnrichmentCache(tmp_path),
        extractor=extractor,
        chunker=chunker,
        policy=policy,
    )

    first = enricher.enrich(make_preprocessing_result())
    second = enricher.enrich(make_preprocessing_result())

    assert first.candidates[0].status == EnrichmentStatus.ENRICHED
    assert first.candidates[0].input_strategy == EnrichmentInputStrategy.FULL_CONTENT
    assert first.candidates[0].document is not None
    assert first.records[0].cache_hit is False
    assert second.records[0].cache_hit is True
    assert fetcher.calls == 1
