from app.research.models import Claim
from app.research.matcher import group_similar_claims


claims = [

    Claim(
        statement="Chennai drainage network gaps were reduced.",
        sources=[
            "https://www.thehindu.com/article1"
        ],
    ),

    Claim(
        statement="The number of stormwater drainage gaps in Chennai has decreased.",
        sources=[
            "https://www.newindianexpress.com/article2"
        ],
    ),

    Claim(
        statement="Chennai cricket team won the match yesterday.",
        sources=[
            "https://www.news18.com/article3"
        ],
    ),
]


groups = group_similar_claims(
    claims,
    threshold=0.35,
)


print(f"Groups found: {len(groups)}")


for index, group in enumerate(groups, start=1):

    print(f"\nGroup {index}")
    print("-" * 40)

    for claim in group:

        print(f"Statement: {claim.statement}")

        print(
            f"Source: {claim.sources[0]}"
        )