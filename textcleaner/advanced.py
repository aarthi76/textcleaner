from textblob import TextBlob

def correct_spelling(text: str) -> str
    """Fix spelling errors using TextBlob."""
    return str(TextBlob(text).correct())

def remove_profanity(text: str, custom_words: list = None) -> str:
    """Filter out profanity (with custom blocklist)"""
    from better_profanity import profanity
    profanity.load_censor_words()
    if custom_words:
        profanity.add_censor_words(custom_words)
    return profanity.censor(text)