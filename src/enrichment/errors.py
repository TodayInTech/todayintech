from src.enrichment.models import EnrichmentFailureReason


class EnrichmentError(Exception):
    def __init__(
        self,
        reason: EnrichmentFailureReason,
        detail: str,
        *,
        http_status: int | None = None,
        content_type: str | None = None,
    ) -> None:
        super().__init__(detail)
        self.reason = reason
        self.detail = detail
        self.http_status = http_status
        self.content_type = content_type
