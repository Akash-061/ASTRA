import os

import requests
from dotenv import load_dotenv

from app.research.models import SearchResult


load_dotenv()


def deduplicate_results(
    results: list[SearchResult],
) -> list[SearchResult]:

    unique_results = []
    seen_urls = set()

    for result in results:

        url = result.url.strip().lower()

        if not url:
            continue

        if url in seen_urls:
            continue

        seen_urls.add(url)
        unique_results.append(result)

    return unique_results


def search_web(query: str) -> list[SearchResult]:

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise RuntimeError(
            "TAVILY_API_KEY is not configured."
        )

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic",
        "max_results": 5,
    }

    response = requests.post(
        url,
        json=payload,
        timeout=15,
    )

    response.raise_for_status()

    data = response.json()

    results = []

    for item in data.get("results", []):

        results.append(
            SearchResult(
                title=item.get("title", ""),
                url=item.get("url", ""),
                snippet=item.get("content", ""),
                source=item.get("url", ""),
                published_date=item.get("published_date"),
)
        )

    return deduplicate_results(results)