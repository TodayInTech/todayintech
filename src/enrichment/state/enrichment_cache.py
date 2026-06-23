import hashlib
import json
from pathlib import Path

from src.enrichment.contracts import BaseEnrichmentCache
from src.enrichment.models import EnrichedArticleCandidate
from src.processing.models import ArticleCandidate


class JsonEnrichmentCache(BaseEnrichmentCache):
    def __init__(self, cache_dir: Path) -> None:
        self.cache_dir = cache_dir

    def build_key(
        self,
        candidate: ArticleCandidate,
        *,
        extractor_name: str,
        extractor_version: str,
        chunker_name: str,
        policy_name: str,
        policy_version: str,
    ) -> str:
        raw_key = "|".join(
            [
                candidate.normalized_url,
                extractor_name,
                extractor_version,
                chunker_name,
                policy_name,
                policy_version,
            ]
        )
        return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()

    def get(self, key: str) -> EnrichedArticleCandidate | None:
        path = self.cache_dir / f"{key}.json"
        if not path.exists():
            return None
        try:
            return EnrichedArticleCandidate.model_validate_json(path.read_text(encoding="utf-8"))
        except ValueError:
            return None

    def save(self, key: str, candidate: EnrichedArticleCandidate) -> None:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        path = self.cache_dir / f"{key}.json"
        path.write_text(
            json.dumps(candidate.model_dump(mode="json"), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
