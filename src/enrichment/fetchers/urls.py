from urllib.parse import urlsplit, urlunsplit


def download_url(url: str) -> str:
    """Resolve public GitHub PDF viewers to the repository's original file."""
    parts = urlsplit(url)
    path = parts.path.split("/")
    if (
        parts.hostname == "github.com"
        and len(path) >= 6
        and path[3] == "blob"
        and parts.path.lower().endswith(".pdf")
    ):
        return urlunsplit(
            ("https", "raw.githubusercontent.com", "/".join(path[1:3] + path[4:]), "", "")
        )
    return url


def alternate_article_url(url: str) -> str | None:
    """Retry the publisher's canonical slash form, never a proxy or challenge bypass."""
    parts = urlsplit(url)
    if (
        parts.hostname == "openai.com"
        and parts.path.startswith("/index/")
        and not parts.path.endswith("/")
    ):
        return urlunsplit((parts.scheme, parts.netloc, parts.path + "/", parts.query, ""))
    return None
