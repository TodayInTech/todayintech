import base64
from io import BytesIO

import pytest
from pypdf import PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

from src.enrichment.errors import EnrichmentError
from src.enrichment.extractors.pdf import PdfContentExtractor
from src.enrichment.factories.extractor_factory import ContentExtractorFactory
from src.enrichment.models import EnrichmentFailureReason, FetchedContent
from src.enrichment.tokenization import TiktokenTokenCounter


def make_pdf(*, encrypted=False, text=True):
    writer = PdfWriter()
    page = writer.add_blank_page(width=612, height=792)
    if text:
        font = DictionaryObject(
            {
                NameObject("/Type"): NameObject("/Font"),
                NameObject("/Subtype"): NameObject("/Type1"),
                NameObject("/BaseFont"): NameObject("/Helvetica"),
            }
        )
        page[NameObject("/Resources")] = DictionaryObject(
            {NameObject("/Font"): DictionaryObject({NameObject("/F1"): writer._add_object(font)})}
        )
        stream = DecodedStreamObject()
        stream.set_data(
            b"BT /F1 12 Tf 72 720 Td (Evidence from the original research paper.) Tj ET"
        )
        page[NameObject("/Contents")] = writer._add_object(stream)
    if encrypted:
        writer.encrypt("password")
    output = BytesIO()
    writer.write(output)
    return FetchedContent(
        source_url="https://example.com/paper.pdf",
        final_url="https://example.com/paper.pdf",
        http_status=200,
        content_type="application/pdf",
        body="",
        binary_base64=base64.b64encode(output.getvalue()).decode(),
        response_bytes=len(output.getvalue()),
        duration_ms=0,
    )


def test_default_router_extracts_pdf_text():
    document = (
        ContentExtractorFactory()
        .create("auto", token_counter=TiktokenTokenCounter())
        .extract(make_pdf())
    )
    assert document.document_type == "pdf"
    assert document.extraction_method == "pdf_text"
    assert "original research paper" in document.plain_text
    assert document.token_count > 0


@pytest.mark.parametrize(
    ("kwargs", "reason"),
    [
        ({"encrypted": True}, EnrichmentFailureReason.POLICY_REJECTED),
        ({"text": False}, EnrichmentFailureReason.EMPTY_CONTENT),
    ],
)
def test_unreadable_pdf_is_explicit_failure(kwargs, reason):
    with pytest.raises(EnrichmentError) as error:
        PdfContentExtractor(TiktokenTokenCounter()).extract(make_pdf(**kwargs))
    assert error.value.reason == reason
