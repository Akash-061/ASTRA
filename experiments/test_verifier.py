from app.research.models import Claim
from app.research.verifier import verify_claims


claims = [

    Claim(
        statement="Chennai officials announced a new project.",
        sources=[
            "https://example.com/article"
        ],
    ),

    Claim(
        statement="Chennai officials announced a new project.",
        sources=[
            "https://news.com/chennai"
        ],
    ),

    Claim(
        statement="Chennai officials announced a new project.",
        sources=[
            "https://another.com/news"
        ],
    ),
]


verified = verify_claims(claims)


for claim in verified:

    print("\nStatement:")
    print(claim.statement)

    print("\nSources:")

    for source in claim.sources:
        print(source)

    print(
        f"\nConfidence: {claim.confidence}"
    )