from typing import NotRequired, TypedDict


class SourceConfig(TypedDict):
    url_prefixes: NotRequired[tuple[str, ...]]
    collection_limit: NotRequired[int]
    lookback_days: NotRequired[int]
