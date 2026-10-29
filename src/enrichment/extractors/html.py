import hashlib
import json
from xml.etree import ElementTree

import trafilatura
from lxml import html
from lxml.etree import ParserError
from trafilatura import __version__ as trafilatura_version

from src.enrichment.contracts import BaseContentExtractor, BaseTokenCounter
from src.enrichment.errors import EnrichmentError
from src.enrichment.models import (
    DocumentBlock,
    DocumentBlockType,
    EnrichmentFailureReason,
    ExtractedDocument,
    FetchedContent,
)

BLOCK_TAGS = {
    "head": DocumentBlockType.HEADING,
    "p": DocumentBlockType.PARAGRAPH,
    "item": DocumentBlockType.LIST_ITEM,
    "code": DocumentBlockType.CODE,
    "quote": DocumentBlockType.QUOTE,
    "table": DocumentBlockType.TABLE,
}


class HtmlContentExtractor(BaseContentExtractor):
    name = "trafilatura"
    version = f"{trafilatura_version}-recovery-1"

    def __init__(self, token_counter: BaseTokenCounter, minimum_tokens: int = 100) -> None:
        self.token_counter = token_counter
        self.minimum_tokens = minimum_tokens

    def extract(self, fetched: FetchedContent) -> ExtractedDocument:
        # Challenge/session pages must never become evidence, even if long enough.
        try:
            page = html.fromstring(fetched.body)
            title = " ".join(page.xpath("//title/text()")).lower()
        except ValueError, ParserError:
            title = ""
        if any(
            marker in title
            for marker in ("just a moment", "access denied", "security check", "sign in to github")
        ):
            raise EnrichmentError(
                EnrichmentFailureReason.ACCESS_DENIED,
                "Publisher returned a challenge or login page",
            )
        primary = None
        primary_error = None
        try:
            primary = self._extract(fetched, favor_precision=True)
        except EnrichmentError as exc:
            primary_error = exc
        if primary is not None and primary.token_count >= self.minimum_tokens:
            return primary
        try:
            alternate = self._extract(fetched, favor_precision=False)
        except EnrichmentError:
            if primary is not None:
                return primary
            assert primary_error is not None
            raise primary_error from None
        if alternate.token_count >= self.minimum_tokens and (
            primary is None or alternate.token_count > primary.token_count
        ):
            return alternate
        if primary is not None:
            return primary
        return alternate

    def _extract(self, fetched: FetchedContent, *, favor_precision: bool) -> ExtractedDocument:
        xml_output = trafilatura.extract(
            fetched.body,
            output_format="xml",
            with_metadata=True,
            include_comments=False,
            include_tables=True,
            include_links=False,
            favor_precision=favor_precision,
            url=fetched.final_url,
        )
        metadata_output = trafilatura.extract(
            fetched.body,
            output_format="json",
            with_metadata=True,
            include_comments=False,
            include_tables=True,
            favor_precision=favor_precision,
            url=fetched.final_url,
        )
        if not xml_output:
            raise EnrichmentError(
                EnrichmentFailureReason.EXTRACTION_FAILED,
                "Trafilatura returned no extractable content",
            )

        try:
            root = ElementTree.fromstring(xml_output)
        except ElementTree.ParseError as exc:
            raise EnrichmentError(
                EnrichmentFailureReason.EXTRACTION_FAILED,
                "Trafilatura XML output could not be parsed",
            ) from exc

        metadata = json.loads(metadata_output) if metadata_output else {}
        blocks = self._build_blocks(root)
        plain_text = "\n\n".join(block.text for block in blocks if block.text).strip()
        if not plain_text:
            raise EnrichmentError(
                EnrichmentFailureReason.EMPTY_CONTENT,
                "Extracted document contains no text blocks",
            )

        return ExtractedDocument(
            extraction_method="precision" if favor_precision else "balanced_retry",
            title=metadata.get("title"),
            author=metadata.get("author"),
            published_at=metadata.get("date"),
            detected_language=metadata.get("language"),
            plain_text=plain_text,
            content_hash=hashlib.sha256(plain_text.encode("utf-8")).hexdigest(),
            char_count=len(plain_text),
            token_count=self.token_counter.count(plain_text),
            blocks=blocks,
        )

    def _build_blocks(self, root: ElementTree.Element) -> list[DocumentBlock]:
        blocks: list[DocumentBlock] = []
        heading_path: list[str] = []
        seen_signatures: set[tuple[DocumentBlockType, str]] = set()
        for element in root.iter():
            tag = element.tag.rsplit("}", 1)[-1]
            block_type = BLOCK_TAGS.get(tag)
            if block_type is None:
                continue
            text = " ".join("".join(element.itertext()).split())
            if not text:
                continue
            signature = (block_type, text)
            if signature in seen_signatures:
                continue
            seen_signatures.add(signature)
            if block_type == DocumentBlockType.HEADING:
                heading_path = [text]
            blocks.append(
                DocumentBlock(
                    block_id=f"block-{len(blocks) + 1:04d}",
                    block_type=block_type,
                    heading_path=list(heading_path),
                    text=text,
                    position=len(blocks),
                    token_count=self.token_counter.count(text),
                )
            )
        return blocks
