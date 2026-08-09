from app.research.models import Claim
from app.research.verifier import verify_claims


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
        statement="Stormwater drainage gaps in Chennai were reduced.",
        sources=[
            "https://www.news18.com/article3"
        ],
    ),

    Claim(
        statement="Chennai cricket team won the match yesterday.",
        sources=[
            "https://www.espncricinfo.com/article4"
        ],
    ),
]


verified = verify_claims(
    claims,
    similarity_threshold=0.35,
)


print(f"Evidence groups: {len(verified)}")


for index, group in enumerate(
    verified,
    start=1,
):

    print(f"\nGroup {index}")
    print("-" * 40)

    print(
        f"Representative: "
        f"{group.representative_claim}"
    )

    print(
        f"Related claims: "
        f"{len(group.claims)}"
    )

    print(
        f"Sources: "
        f"{len(group.sources)}"
    )

    print(
        f"Domains: "
        f"{len(group.domains)}"
    )

    print(
        f"Confidence: "
        f"{group.confidence:.0%}"
    )

    for source in group.sources:
        print(f"  - {source}")