from app.research.models import SearchResult
from app.research.analyzer import extract_claims


result = SearchResult(
    title="Chennai News",
    url="https://example.com/chennai",
    snippet=(
        "Power outages affected several areas of Chennai. "
        "Residents in Adyar reported frequent interruptions. "
        "Looking for more such exciting and meaningful stories? "
        "Grab our latest issue on Amazon. "
        "Email us your question at test@example.com. "
        "The Greater Chennai Corporation said repairs were underway. "
        "Read More. "
        "Subscribe to continue reading."
    ),
)


claims = extract_claims([result])


print(f"Claims found: {len(claims)}")

for index, claim in enumerate(
    claims,
    start=1,
):

    print(f"\nClaim {index}:")
    print(claim.statement)