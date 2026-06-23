import tiktoken

from src.enrichment.contracts import BaseTokenCounter


class TiktokenTokenCounter(BaseTokenCounter):
    name = "tiktoken:o200k_base"

    def __init__(self, encoding_name: str = "o200k_base") -> None:
        self.encoding = tiktoken.get_encoding(encoding_name)
        self.name = f"tiktoken:{encoding_name}"

    def count(self, text: str) -> int:
        return len(self.encoding.encode(text))
