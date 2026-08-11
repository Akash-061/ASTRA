from app.research.models import Claim

from app.research.verifier import (
    verify_claims,
)


claims = [

    Claim(
        statement=(
            "Chennai airport operations "
            "resumed normally."
        ),
        sources=[
            "https://www.reuters.com/"
            "world/asia/chennai-airport"
        ],
        source_title=(
            "Reuters: Chennai airport resumes"
        ),
        source_url=(
            "https://www.reuters.com/"
            "world/asia/chennai-airport"
        ),
    ),

    Claim(
        statement=(
            "Chennai airport operations "
            "remain disrupted."
        ),
        sources=[
            "https://www.bbc.com/"
            "news/world/asia/chennai-airport"
        ],
        source_title=(
            "BBC: Chennai airport disruption"
        ),
        source_url=(
            "https://www.bbc.com/"
            "news/world/asia/chennai-airport"
        ),
    ),

    Claim(
        statement=(
            "Airport operations resumed "
            "normally after the disruption."
        ),
        sources=[
            "https://www.apnews.com/"
            "article/chennai-airport"
        ],
        source_title=(
            "AP: Chennai airport update"
        ),
        source_url=(
            "https://www.apnews.com/"
            "article/chennai-airport"
        ),
    ),
]


groups = verify_claims(
    claims
)


print()
print("================================")
print("CONFLICT-AWARE VERIFIER")
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
    "Domains:",
    len(group.domains)
)

print(
    "Has conflict:",
    group.has_conflict
)

print(
    "Conflicting claims:",
    len(
        group.conflicting_claims
    )
)

print(
    "Confidence:",
    f"{group.confidence:.3f}"
)


assert group.has_conflict is True

assert (
    len(
        group.conflicting_claims
    )
    >= 2
)

assert (
    group.confidence < 0.85
)


print()
print(
    "CONFLICT-AWARE VERIFIER PASSED"
)