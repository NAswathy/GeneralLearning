import logging
from typing import Any

import feedparser
from mcp.server.fastmcp import FastMCP


logging.basicConfig(level=logging.INFO)

mcp = FastMCP("General Knowledge News Server")

GOOGLE_NEWS_RSS = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"


@mcp.tool()
def get_top_headlines(limit: int = 10) -> list[dict[str, Any]]:
    """Return recent Google News headlines for current-affairs style question generation."""
    feed = feedparser.parse(GOOGLE_NEWS_RSS)

    headlines = []
    for entry in feed.entries[:limit]:
        headlines.append(
            {
                "title": getattr(entry, "title", "").strip(),
                "link": getattr(entry, "link", "").strip(),
                "published": getattr(entry, "published", "").strip(),
                "summary": getattr(entry, "summary", "").strip(),
            }
        )

    return headlines


if __name__ == "__main__":
    mcp.run(transport="stdio")
