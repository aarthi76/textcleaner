from textcleaner import clean_text

def test_clean_text():
    dirty_text = "Check this out: https://example.com 😊"
    cleaned = clean_text(dirty_text)
    assert "https://" not in cleaned
    assert "😊" not in cleaned