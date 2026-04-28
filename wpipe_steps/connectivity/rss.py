import feedparser
from typing import Any, Dict, Optional, List
from wpipe_steps.core.base import BaseStep

class RSSParserStep(BaseStep):
    """
    Step for parsing RSS/Atom feeds.
    Extracts entries from a given URL and filters them if necessary.
    """
    
    def __init__(
        self, 
        feed_url: str, 
        limit: int = 5,
        user_agent: str = "wpipe-steps/1.0",
        response_key: str = "rss_entries",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.feed_url = feed_url
        self.limit = limit
        self.user_agent = user_agent
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Use user_agent to avoid blocks from some servers
            feed = feedparser.parse(self.feed_url, agent=self.user_agent)
            
            if feed.get("bozo", 0) == 1 and not feed.entries:
                raise RuntimeError(f"RSS Parsing error (Bozo bit set): {feed.get('bozo_exception')}")

            entries = []
            for entry in feed.entries[:self.limit]:
                entries.append({
                    "title": entry.get("title"),
                    "link": entry.get("link"),
                    "published": entry.get("published"),
                    "summary": entry.get("summary", "")[:200] + "..." # Truncate summary
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
