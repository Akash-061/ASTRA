from app.research.models import SearchResult
from app.research.analyzer import extract_claims


results = [

    SearchResult(
        title="Chennai News",
        url="https://example.com/article",
        snippet="Officials announced a new project in Chennai.",
    ),

    SearchResult(
        title="Another Chennai Report",
        url="https://example.org/article",
        snippet="Residents reported problems in the area.",
    ),
]


claims = extract_claims(results)


print(f"Claims found: {len(claims)}")

for index, claim in enumerate(claims, start=1):

    print(f"\nClaim {index}:")
    print(f"Statement: {claim.statement}")
    print(f"Sources: {claim.sources}")
    print(f"Confidence: {claim.confidence}")