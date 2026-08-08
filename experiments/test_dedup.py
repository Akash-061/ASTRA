from app.research.models import SearchResult
from app.research.search import deduplicate_results


results = [

    SearchResult(
        title="Article One",
        url="https://example.com/article",
        snippet="First article",
    ),

    SearchResult(
        title="Article One Duplicate",
        url="https://example.com/article",
        snippet="Duplicate article",
    ),

    SearchResult(
        title="Article Two",
        url="https://another.com/article",
        snippet="Second article",
    ),
]


unique_results = deduplicate_results(results)


print(f"Original results: {len(results)}")
print(f"Unique results: {len(unique_results)}")

for result in unique_results:
    print(result.title)