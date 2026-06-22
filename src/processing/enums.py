from enum import StrEnum


class ExcludedReason(StrEnum):
    INVALID_ARTICLE = "invalid_article"
    DUPLICATE_IN_RUN = "duplicate_in_run"
    ALREADY_BRIEFED = "already_briefed"
    SERVICE_CANDIDATE_LIMIT = "service_candidate_limit"
    TOTAL_CANDIDATE_LIMIT = "total_candidate_limit"
