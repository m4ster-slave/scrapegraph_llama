import json
import os
import sys
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph
import nest_asyncio
nest_asyncio.apply()

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")

if not OLLAMA_URL:
    print("Error: OLLAMA_URL not set in .env file.")
    sys.exit(1)

if len(sys.argv) != 3:
    print("Usage: python script.py <prompt> <source>")
    print("Example: python script.py 'What does the company do?' 'https://example.com'")
    sys.exit(1)

prompt = sys.argv[1]
source = sys.argv[2]

graph_config = {
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",
        "base_url": OLLAMA_URL,
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": OLLAMA_URL,
    }
}

smart_scraper_graph = SmartScraperGraph(
    prompt=prompt,
    source=source,
    config=graph_config
)

try:
    result = smart_scraper_graph.run()
    print(json.dumps(result, indent=4))
except Exception as e:
    print(f"Error running SmartScraperGraph: {e}")
