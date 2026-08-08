from app.research.models import SearchResult
from app.research.source import get_domain, group_by_domain


results = [

    SearchResult(
        title="Hindu Article 1",
        url="https://www.thehindu.com/news/chennai/article1",
    ),

    SearchResult(
        title="Hindu Article 2",
        url="https://www.thehindu.com/cities/chennai/article2",
    ),

    SearchResult(
        title="News18 Article",
        url="https://www.news18.com/chennai/article3",
    ),
]


print("Domains:")

for result in results:
    print(get_domain(result.url))


groups = group_by_domain(results)

print("\nGrouped results:")

for domain, domain_results in groups.items():

    print(f"{domain}: {len(domain_results)} result(s)")