"""
RSS Parser Step - Parse RSS/Atom feeds and extract entries.
"""

import feedparser
from typing import Any, Dict, List, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep


class RSSContext(BaseModel):
    """Context for RSS parsing operations."""
    feed_url: str
    limit: int = 5
    user_agent: str = "wpipe-steps/1.0"


@step(
    name="rss_parser",
    version="v1.0",
    description="RSS feed parser",
    tags=["connectivity", "rss", "feed", "sync"]
)
class RSSParserStep(BaseStep):
    """Step for parsing RSS/Atom feeds.
    
    Extracts entries from a given URL and filters them if necessary.
    """

    def __init__(
        self,
        response_key: str = "rss_entries",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__()
        self.response_key = response_key
        self.name = name or "rss_parser"
        self.version = version

    @to_obj(RSSContext)
    def __call__(self, data: RSSContext) -> Dict[str, Any]:
        """Parse RSS feed and extract entries.
        
        Args:
            data: Context containing feed_url, limit, user_agent.
            
        Returns:
            Dictionary with operation result.
        """
        try:
            # Use user_agent to avoid blocks from some servers
            feed = feedparser.parse(data.feed_url, agent=data.user_agent)
            
            if feed.get("bozo", 0) == 1 and not feed.entries:
                raise RuntimeError(f"RSS Parsing error (Bozo bit set): {feed.get('bozo_exception')}")
            
            entries = []
            for entry in feed.entries[:data.limit]:
                entries.append({
                    "title": entry.get("title"),
                    "link": entry.get("link"),
                    "published": entry.get("published"),
                    "summary": entry.get("summary", "")[:200] + "..."  # Truncate summary
                })
            
            data[self.response_key] = {
                "success": True,
                "feed_title": feed.feed.get("title", "Unknown Feed"),
                "entries": entries,
                "count": len(entries)
            }
            
            return data
            
        except Exception as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"RSS Parsing failed: {str(e)}")
