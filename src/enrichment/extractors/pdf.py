import base64
import hashlib
from io import BytesIO

from pypdf import PdfReader, __version__
from pypdf.errors import PyPdfError

from src.enrichment.contracts import BaseContentExtractor, BaseTokenCounter
from src.enrichment.errors import EnrichmentError
from src.enrichment.models import (
    DocumentBlock,
    DocumentBlockType,
    EnrichmentFailureReason,
    ExtractedDocument,
    FetchedContent,
)


class PdfContentExtractor(BaseContentExtractor):
    name = "pypdf"
    version = __version__

    def __init__(self, token_counter: BaseTokenCounter) -> None:
        self.token_counter = token_counter

    def extract(self, fetched: FetchedContent) -> ExtractedDocument:
        try:
            reader = PdfReader(
                BytesIO(base64.b64decode(fetched.binary_base64 or "", validate=True))
            )
            if reader.is_encrypted or len(reader.pages) > 100:
                raise EnrichmentError(
                    EnrichmentFailureReason.POLICY_REJECTED,
                    "Encrypted PDF or PDF exceeds 100 page limit",
                )
            blocks = []
            for index, page in enumerate(reader.pages):
                contents = page.get_contents()
                if contents is not None and len(contents.get_data()) > 10 * 1024 * 1024:
                    raise EnrichmentError(
                        EnrichmentFailureReason.POLICY_REJECTED, "PDF page exceeds extraction limit"
                    )
                text = (page.extract_text() or "").strip()
                if text:
                    blocks.append(
                        DocumentBlock(
                            block_id=f"page-{index + 1:04d}",
                            block_type=DocumentBlockType.PARAGRAPH,
                            heading_path=[],
                            text=text,
                            position=len(blocks),
                            token_count=self.token_counter.count(text),
                        )
                    )
        except (PyPdfError, ValueError, TypeError, KeyError, OSError) as exc:
            raise EnrichmentError(
                EnrichmentFailureReason.EXTRACTION_FAILED,
                f"PDF extraction failed: {type(exc).__name__}",
            ) from exc
        plain_text = "\n\n".join(block.text for block in blocks)
        if not plain_text:
            raise EnrichmentError(
                EnrichmentFailureReason.EMPTY_CONTENT,
                "PDF has no extractable text; OCR is not enabled",
            )
        # PDF metadata titles are often filenames or TeX defaults; validate evidence downstream.
        return ExtractedDocument(
            title=None,
            document_type="pdf",
            extraction_method="pdf_text",
            plain_text=plain_text,
            content_hash=hashlib.sha256(plain_text.encode()).hexdigest(),
            char_count=len(plain_text),
            token_count=self.token_counter.count(plain_text),
            blocks=blocks,
        )
