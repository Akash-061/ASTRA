from app.research.models import (
    Claim,
    EvidenceGroup,
)

from app.research.synthesis import (
    synthesize_answer,
)


claim_a = Claim(
    statement=(
        "Chennai airport operations "
        "resumed normally."
    ),
    sources=[
        "https://example.com/resumed"
    ],
)

claim_b = Claim(
    statement=(
        "Chennai airport operations "
        "remain disrupted."
    ),
    sources=[
        "https://example.org/disrupted"
    ],
)


group = EvidenceGroup(
    representative_claim=(
        claim_a.statement
    ),
    claims=[
        claim_a,
        claim_b,
    ],
    sources=[
        "https://example.com/resumed",
        "https://example.org/disrupted",
    ],
    domains=[
        "example.com",
        "example.org",
    ],
    confidence=0.40,
    has_conflict=True,
    conflicting_claims=[
        claim_a,
        claim_b,
    ],
)


answer = synthesize_answer(
    "Chennai airport status",
    [group],
)


print()
print("================================")
print("CONFLICT SYNTHESIS TEST")
print("================================")
print()
print(answer)
print()


assert (
    "Conflict detected"
    in answer
)

assert (
    "sources disagree"
    in answer
)

assert (
    claim_a.statement
    in answer
)

assert (
    claim_b.statement
    in answer
)


print(
    "CONFLICT SYNTHESIS PASSED"
)