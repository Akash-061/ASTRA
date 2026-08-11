from app.research.models import Claim
from app.research.verifier import verify_claims


claims = [
    Claim(
        statement=(
            "Power outages affected residents "
            "in Adyar, Chennai."
        ),
        sources=[
            "https://example.com/chennai/power"
        ],
        source_title=(
            "Chennai power outages affect residents"
        ),
        source_url=(
            "https://example.com/chennai/power"
        ),
    ),

    Claim(
        statement=(
            "Power outages affected residents "
            "in Adyar, Chennai."
        ),
        sources=[
            "https://example.org/chennai/power"
        ],
        source_title=(
            "Adyar residents affected by outages"
        ),
        source_url=(
            "https://example.org/chennai/power"
        ),
    ),

    Claim(
        statement=(
            "Power outages affected residents "
            "in Adyar, Chennai."
        ),
        sources=[
            "https://example.net/chennai/power"
        ],
        source_title=(
            "Chennai electricity outage report"
        ),
        source_url=(
            "https://example.net/chennai/power"
        ),
    ),
]


groups = verify_claims(
    claims
)


print()
print("================================")
print("VERIFIER QUALITY TEST")
print("================================")

print(
    f"Evidence groups: {len(groups)}"
)

for index, group in enumerate(
    groups,
    start=1,
):

    print()
    print(
        f"Group {index}"
    )

    print(
        "Representative:",
        group.representative_claim,
    )

    print(
        "Claims:",
        len(group.claims),
    )

    print(
        "Sources:",
        len(group.sources),
    )

    print(
        "Domains:",
        len(group.domains),
    )

    print(
        "Confidence:",
        f"{group.confidence:.3f}",
    )


assert len(groups) == 1

group = groups[0]

assert len(group.claims) == 3

assert len(group.domains) == 3

assert group.confidence == 0.85


print()
print("VERIFIER BASELINE PASSED")