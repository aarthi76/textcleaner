import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def debug_clean(text: str) -> str:
    """Log cleaning steps for debugging."""
    logger.debug(f"Original text: {text}")
    cleaned = cleaned_text(text)
    logger.debug(f"Cleaned text: {cleaned}")
    return cleaned