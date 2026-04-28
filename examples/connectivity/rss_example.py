import sys
from pathlib import Path

# Add project root to path for local development testing
sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.connectivity import RSSParserStep

def main():
    pipeline = Pipeline(pipeline_name="RSS_Demo", verbose=True)

    # Example: Parse a more stable feed (NASA Breaking News)
    fetch_news = RSSParserStep.as_step(
        name="Fetch_NASA_News",
        feed_url="https://www.nasa.gov/rss/dyn/breaking_news.rss",
        limit=3
    )

    def display_results(data):
        rss = data.get("rss_entries", {})
        if rss.get("success"):
            print(f"\n📰 Feed: {rss['feed_title']}")
            print(f"Total entries found: {rss['count']}")
            for i, entry in enumerate(rss['entries'], 1):
                print(f"  {i}. {entry['title']}")
        else:
            print(f"❌ Error: {rss.get('error')}")
        return data

    pipeline.set_steps([
        fetch_news,
        display_results
    ])

    print("🚀 Running RSS Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
