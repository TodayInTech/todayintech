from src.enrichment.contracts import BaseContentExtractor, BaseTokenCounter
from src.enrichment.extractors import HtmlContentExtractor
from src.enrichment.extractors.pdf import PdfContentExtractor
from src.enrichment.extractors.routing import RoutingContentExtractor


class ContentExtractorFactory:
    _html_content_types = {"text/html", "application/xhtml+xml", ""}

    def create(
        self,
        content_type: str,
        *,
        token_counter: BaseTokenCounter,
        minimum_tokens: int = 100,
    ) -> BaseContentExtractor:
        if content_type in self._html_content_types:
            return HtmlContentExtractor(token_counter, minimum_tokens)
        if content_type == "application/pdf":
            return PdfContentExtractor(token_counter)
        if content_type == "auto":
            return RoutingContentExtractor(token_counter, minimum_tokens)
        raise ValueError(f"Unsupported extractor content type: {content_type}")
