from html import unescape
from html.parser import HTMLParser


class _HtmlTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"br", "li", "p", "div"}:
            self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"li", "p", "div"}:
            self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        self._chunks.append(data)

    def text(self) -> str:
        return "".join(self._chunks)


def strip_html(value: str) -> str:
    parser = _HtmlTextExtractor()
    parser.feed(value)
    parser.close()
    return parser.text()


def normalize_markdown_text(value: str) -> str:
    lines = []
    for line in strip_html(unescape(value)).splitlines():
        normalized = " ".join(line.split())
        if normalized:
            lines.append(normalized)
    return "\n".join(lines)


def normalize_plain_text(value: str) -> str:
    lines = []
    for line in unescape(value).splitlines():
        normalized = " ".join(line.split())
        if normalized:
            lines.append(normalized)
    return "\n".join(lines)


def escape_mdx_text(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("{", "&#123;")
        .replace("}", "&#125;")
    )


def escape_markdown_block_markers(value: str) -> str:
    escaped_lines = []
    for line in value.splitlines():
        if line.startswith(("#", "-", "*", "+", ">")):
            escaped_lines.append(f"\\{line}")
        else:
            escaped_lines.append(line)
    return "\n".join(escaped_lines)


def mdx_safe_text(value: str) -> str:
    return escape_markdown_block_markers(escape_mdx_text(normalize_markdown_text(value)))


def mdx_safe_plain_text(value: str) -> str:
    return escape_mdx_text(normalize_plain_text(value))


def mdx_safe_link_label(value: str) -> str:
    return mdx_safe_plain_text(value).replace("[", "\\[").replace("]", "\\]")
