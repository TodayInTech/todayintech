import re
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


def mdx_safe_article(value: str) -> str:
    """Preserve editorial Markdown while keeping model output inert in MDX.

    Only the generator adds clickable source links. Model-generated links/images
    remain literal text, so URL schemes and reference definitions cannot execute.
    Fenced/inline code stays verbatim; HTML and expressions outside code are text.
    """
    lines: list[str] = []
    fence = ""
    for line in value.replace("\r\n", "\n").replace("\r", "\n").splitlines():
        if fence:
            lines.append(line)
            if re.fullmatch(rf" {{0,3}}{re.escape(fence[0])}{{{len(fence)},}}\s*", line):
                fence = ""
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if opening:
            fence = opening[1]
            language = re.match(r"[a-zA-Z0-9_+-]+", opening[2].strip())
            lines.append(fence + (language[0] if language else ""))
            continue

        # Quote markers are Markdown structure; other angle brackets are text.
        quote = re.match(r"^( {0,3}(?:> ?)+)", line)
        prefix = quote[0] if quote else ""
        text = line[len(prefix) :]
        text = re.sub(r"^( {0,3})#(?=\s)", r"\1##", text)
        parts: list[str] = []
        position = 0
        for code in re.finditer(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)", text):
            preceding = text[: code.start()]
            if (len(preceding) - len(preceding.rstrip("\\"))) % 2:
                continue
            parts.append(_safe_article_text(text[position : code.start()]))
            parts.append(code[0])
            position = code.end()
        parts.append(_safe_article_text(text[position:]))
        lines.append(prefix + "".join(parts))
    if fence:
        lines.append(fence)
    return "\n".join(lines).strip()


def _safe_article_text(value: str) -> str:
    text = escape_mdx_text(value).replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
    return re.sub(
        r"^(\s*)(import|export)\b",
        lambda match: f"{match[1]}&#{ord(match[2][0])};{match[2][1:]}",
        text,
    )
