from app.research.models import SearchResult


result = SearchResult(
    title="Test Article",
    url="https://example.com",
    snippet="This is a test search result.",
    source="Example"
)


print(result)
print(result.title)
print(result.url)
print(result.source)