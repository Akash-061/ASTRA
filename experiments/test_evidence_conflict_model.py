from app.research.models import (
    Claim,
    EvidenceGroup,
)


claim_a = Claim(
    statement=(
        "Chennai airport operations "
        "resumed normally."
    )
)


claim_b = Claim(
    statement=(
        "Chennai airport operations "
        "remain disrupted."
    )
)


group = EvidenceGroup(
    representative_claim=(
        claim_a.statement
    ),
    claims=[
        claim_a,
        claim_b,
    ],
    sources=[],
    domains=[],
    confidence=0.50,
    has_conflict=True,
    conflicting_claims=[
        claim_b,
    ],
)


print()
print("================================")
print("EVIDENCE CONFLICT MODEL")
print("================================")

print(
    "Representative:",
    group.representative_claim,
)

print(
    "Claims:",
    len(group.claims),
)

print(
    "Has conflict:",
    group.has_conflict,
)

print(
    "Conflicting claims:",
    len(
        group.conflicting_claims
    ),
)


assert group.has_conflict is True

assert (
    len(
        group.conflicting_claims
    )
    == 1
)


print()
print(
    "EVIDENCE CONFLICT MODEL PASSED"
)