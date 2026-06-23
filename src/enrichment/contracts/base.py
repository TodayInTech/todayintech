from abc import ABC, abstractmethod

from src.enrichment.context import EnrichmentContext
from src.enrichment.models import (
    EnrichedArticleCandidate,
    EvidenceChunk,
    ExtractedDocument,
    FetchedContent,
)
from src.processing.models import ArticleCandidate


class BaseContentFetcher(ABC):
    name: str

    @abstractmethod
    def fetch(self, url: str) -> FetchedContent:
        """Fetch source content for a URL."""


class BaseContentExtractor(ABC):
    name: str
    version: str

    @abstractmethod
    def extract(self, fetched: FetchedContent) -> ExtractedDocument:
        """Extract a structured document from fetched content."""


class BaseTokenCounter(ABC):
    name: str

    @abstractmethod
    def count(self, text: str) -> int:
        """Count tokens in text."""


class BaseContentChunker(ABC):
    name: str

    @abstractmethod
    def chunk(self, document: ExtractedDocument) -> list[EvidenceChunk]:
        """Split a structured document without summarizing it."""


class BaseEvidenceSelector(ABC):
    name: str
    version: str

    @abstractmethod
    def select(self, context: EnrichmentContext) -> list[EvidenceChunk]:
        """Select source chunks that fit the Writer evidence budget."""


class BaseEnrichmentPolicy(ABC):
    name: str
    version: str

    @abstractmethod
    def decide(self, context: EnrichmentContext) -> EnrichedArticleCandidate:
        """Choose the Writer input strategy for an enriched candidate."""


class BaseEnrichmentCache(ABC):
    @abstractmethod
    def build_key(
        self,
        candidate: ArticleCandidate,
        *,
        extractor_name: str,
        extractor_version: str,
        chunker_name: str,
        policy_name: str,
        policy_version: str,
        selector_name: str,
        selector_version: str,
    ) -> str:
        """Build a stable cache key."""

    @abstractmethod
    def get(self, key: str) -> EnrichedArticleCandidate | None:
        """Return a cached candidate when available."""

    @abstractmethod
    def save(self, key: str, candidate: EnrichedArticleCandidate) -> None:
        """Persist an enriched candidate."""


class BaseEnrichmentStep(ABC):
    name: str

    @abstractmethod
    def process(self, context: EnrichmentContext) -> EnrichmentContext:
        """Process and return enrichment context."""
