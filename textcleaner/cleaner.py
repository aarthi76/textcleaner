import re
import unicodedata

def remove_emojis(text: str) -> str:
    """Remove emojis from a given text."""
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"  # dingbats
        u"\U000024C2-\U0001F251"  # enclosed characters
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", text)

def clean_text(text: str) -> str:
    """Clean text by removing URLs, emojis, and special chars."""
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = remove_emojis(text)
    text = unicodedata.normalize("NFKD", text)  # Normalize unicode
    return text.strip()

import click

@click.command()
@click.argument("text")
def clean_cli(text: str):
    """CLI for textcleaner."""
    print(clean_text(text))

if __name__ == "__main__":
    clean_cli()