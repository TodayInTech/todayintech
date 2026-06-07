from src.collection.factories import CollectorStrategyFactory
from src.sources import NewsSourceFactory


def test_registered_sources_have_required_metadata() -> None:
    factory = NewsSourceFactory()
    strategy_factory = CollectorStrategyFactory()
    service_keys = factory.service_keys()

    assert service_keys
    assert len(service_keys) == len(set(service_keys))

    for service_key in service_keys:
        source = factory.create(service_key)

        assert source.service_key == service_key
        assert source.service_name
        assert source.source_url.startswith("https://")
        assert source.source_config() is not None
        assert strategy_factory.create(source.collector_type)
