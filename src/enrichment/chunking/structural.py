from src.enrichment.contracts import BaseContentChunker
from src.enrichment.models import EvidenceChunk, ExtractedDocument


class StructuralContentChunker(BaseContentChunker):
    def __init__(self, max_tokens: int = 1200) -> None:
        self.max_tokens = max(max_tokens, 1)
        self.name = f"structural:max={self.max_tokens}"

    def chunk(self, document: ExtractedDocument) -> list[EvidenceChunk]:
        chunks: list[EvidenceChunk] = []
        current_blocks = []
        current_tokens = 0

        for block in document.blocks:
            if current_blocks and current_tokens + block.token_count > self.max_tokens:
                chunks.append(self._build_chunk(chunks, current_blocks))
                current_blocks = []
                current_tokens = 0
            current_blocks.append(block)
            current_tokens += block.token_count

        if current_blocks:
            chunks.append(self._build_chunk(chunks, current_blocks))
        return chunks

    def _build_chunk(self, chunks, blocks) -> EvidenceChunk:
        return EvidenceChunk(
            chunk_id=f"chunk-{len(chunks) + 1:04d}",
            heading_path=blocks[0].heading_path,
            text="\n\n".join(block.text for block in blocks),
            block_ids=[block.block_id for block in blocks],
            token_count=sum(block.token_count for block in blocks),
            position=len(chunks),
        )
