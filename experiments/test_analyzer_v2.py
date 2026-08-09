from app.research.models import SearchResult
from app.research.analyzer import extract_claims


results = [

    SearchResult(
        title="Chennai News",
        url="https://example.com/chennai",
        snippet=(
            "Chemical odour continues to affect "
            "residents in OMR. "
            "Officials are investigating the issue. "
            "Read More. "
            "Subscribe to continue reading."
        ),
    ),

    SearchResult(
        title="Chennai Infrastructure",
        url="https://example.org/chennai",
        snippet=(
            "Several street name boards were damaged "
            "in Kodungaiyur. "
            "Residents have requested repairs."
        ),
    ),
]


claims = extract_claims(results)


print(f"Claims found: {len(claims)}")

for index, claim in enumerate(
    claims,
    start=1,
):

    print(f"\nClaim {index}:")
    print(claim.statement)

    print("Source:")
    print(claim.sources[0])