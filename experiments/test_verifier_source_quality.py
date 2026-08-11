from app.research.models import Claim

from app.research.verifier import (
    verify_claims,
)


claims = [

    Claim(
        statement=(
            "Power outages affected residents "
            "in Adyar, Chennai."
        ),
        sources=[
            "https://www.reuters.com/"
            "world/asia/chennai-power",
        ],
        source_title=(
            "Reuters: Chennai power outages"
        ),
        source_url=(
            "https://www.reuters.com/"
            "world/asia/chennai-power"
        ),
    ),

    Claim(
        statement=(
            "Power outages affected residents "
            "in Adyar, Chennai."
        ),
        sources=[
            "https://www.bbc.com/"
            "news/world/asia/chennai-power",
        ],
        source_title=(
            "BBC: Chennai power outages"
        ),
        source_url=(
            "https://www.bbc.com/"
            "news/world/asia/chennai-power"
        ),
    ),

    Claim(
        statement=(
            "Power outages affected residents "
            "in Adyar, Chennai."
        ),
        sources=[
            "https://www.apnews.com/"
            "article/chennai-power",
        ],
        source_title=(
            "AP: Chennai power outages"
        ),
        source_url=(
            "https://www.apnews.com/"
            "article/chennai-power"
        ),
    ),
]


groups = verify_claims(
    claims
)


print()
print("================================")
print("SOURCE QUALITY VERIFICATION")
print("================================")


print(
    f"Evidence groups: "
    f"{len(groups)}"
)


assert len(groups) == 1


group = groups[0]


print(
    "Claims:",
    len(group.claims)
)

print(
    "Sources:",
    len(group.sources)
)

print(
    "Domains:",
    len(group.domains)
)

print(
    "Confidence:",
    f"{group.confidence:.3f}"
)


assert len(group.claims) == 3

assert len(group.domains) == 3

assert group.confidence > 0.85

assert group.confidence <= 1.0


print()
print(
    "SOURCE QUALITY VERIFICATION PASSED"
)