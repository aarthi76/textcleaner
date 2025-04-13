import re
import unicodedata
from typing import Set

def remove_emojis(text: str, allowed_emojis: Set[str] = None) -> str:
    """
    Remove emojis from text except those in allowed_emojis.
    
    Args:
        text: Input string to clean.
        allowed_emojis: Set of emojis to preserve (e.g., {"👍", "❤️"}).
    
    Returns:
        str: Text with unwanted emojis removed.
    """
    if allowed_emojis is None:
        allowed_emojis = set()
    
    # Unicode ranges for common emoji categories
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # misc symbols
        u"\U00002702-\U000027B0"
        "]+", 
        flags=re.UNICODE,
    )
    
    # Preserve allowed emojis by temporarily replacing them
    placeholder = "█"
    preserved = {}
    for i, emoji in enumerate(allowed_emojis):
        if emoji in text:
            preserved[f"{placeholder}{i}"] = emoji
            text = text.replace(emoji, f"{placeholder}{i}")
    
    # Remove all emojis
    text = emoji_pattern.sub("", text)
    
    # Restore allowed emojis
    for placeholder_str, emoji in preserved.items():
        text = text.replace(placeholder_str, emoji)
    
    return text

def clean_text(text: str) -> str:
    """Clean text by removing URLs, emojis, and special chars."""
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = remove_emojis(text)
    text = unicodedata.normalize("NFKD", text)  # Normalize unicode
    return text.strip()

import click

@click.command()
@click.argument("text")
@click.option("--keep-emojis", help="Comma-separated emojis to preserve (e.g., '❤️,🚀')")
def clean_cli(text: str):
    """CLI for textcleaner."""
    print(clean_text(text))

if __name__ == "__main__":
    clean_cli()