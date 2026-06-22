from src.processing.identity.url_normalizer import normalize_url, title_fingerprint


def test_normalize_url_removes_tracking_params_and_fragment() -> None:
    url = "https://Example.com/Post/?utm_source=hn&ref=feed&id=1#comments"

    assert normalize_url(url) == "https://example.com/Post?id=1"


def test_title_fingerprint_normalizes_case_and_punctuation() -> None:
    assert title_fingerprint("OpenAI: New Agent Feature!") == "openai new agent feature"
