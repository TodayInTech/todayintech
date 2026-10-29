from src.enrichment.contracts import BaseContentExtractor, BaseTokenCounter
from src.enrichment.extractors.html import HtmlContentExtractor
from src.enrichment.extractors.pdf import PdfContentExtractor
from src.enrichment.models import ExtractedDocument, FetchedContent


class RoutingContentExtractor(BaseContentExtractor):
    name = "html-pdf"

    def __init__(self, token_counter: BaseTokenCounter, minimum_tokens: int = 100) -> None:
        self.html = HtmlContentExtractor(token_counter, minimum_tokens)
        self.pdf = PdfContentExtractor(token_counter)
        self.version = f"{self.html.version}-{self.pdf.version}-min{minimum_tokens}"

    def extract(self, fetched: FetchedContent) -> ExtractedDocument:
        if fetched.content_type == "application/pdf":
            return self.pdf.extract(fetched)
        return self.html.extract(fetched)
