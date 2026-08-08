from app.research.search import search_web


results = search_web("recent issues in Chennai")

print(f"\nResults found: {len(results)}\n")


for index, result in enumerate(results, start=1):

    print(f"{index}. {result.title}")
    print(f"   Source: {result.source}")
    print(f"   URL: {result.url}")
    print(f"   {result.snippet[:200]}...")
    print()