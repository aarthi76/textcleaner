import aiohttp
import re

async def clean_webpage(url: str) -> str:
    """Fetch and clean text from a webpage."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
        return clean_text(re.sub(r'<[^>]+>', '', html))  # Remove HTML tags 