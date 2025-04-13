from textcleaner import clean_text, remove_emojis

def test_clean_text():
    dirty_text = "Check this out: https://example.com 😊"
    cleaned = clean_text(dirty_text)
    assert "https://" not in cleaned
    assert "😊" not in cleaned

def test_allowed_emojis():
    text = "Keep ❤️ and 🚀, remove 😊"
    assert remove_emojis(text, allowed_emojis={"❤️", "🚀"}) == "Keep ❤️ and 🚀, remove "