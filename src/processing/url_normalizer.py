import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING_QUERY_PREFIXES = ("utm_",)
TRACKING_QUERY_NAMES = {
    "fbclid",
    "gclid",
    "igshid",
    "mc_cid",
    "mc_eid",
    "ref",
    "ref_src",
}


def normalize_url(value: str) -> str:
    parsed = urlsplit(value.strip())
    scheme = parsed.scheme.lower() or "https"
    netloc = parsed.netloc.lower()
    path = parsed.path.rstrip("/") or "/"

    query_items = []
    for key, query_value in parse_qsl(parsed.query, keep_blank_values=False):
        normalized_key = key.lower()
        if normalized_key in TRACKING_QUERY_NAMES:
            continue
        if any(normalized_key.startswith(prefix) for prefix in TRACKING_QUERY_PREFIXES):
            continue
        query_items.append((key, query_value))

    query = urlencode(sorted(query_items))
    return urlunsplit((scheme, netloc, path, query, ""))


def title_fingerprint(value: str) -> str:
    normalized = value.lower()
    normalized = re.sub(r"[^a-z0-9가-힣]+", " ", normalized)
    return " ".join(normalized.split())
