from src.enrichment.contracts import BaseContentExtractor, BaseTokenCounter
from src.enrichment.extractors import HtmlContentExtractor


class ContentExtractorFactory:
    _html_content_types = {"text/html", "application/xhtml+xml", ""}

    def create(
        self,
        content_type: str,
        *,
        token_counter: BaseTokenCounter,
    ) -> BaseContentExtractor:
        if content_type in self._html_content_types:
            return HtmlContentExtractor(token_counter)
        raise ValueError(f"Unsupported extractor content type: {content_type}")
