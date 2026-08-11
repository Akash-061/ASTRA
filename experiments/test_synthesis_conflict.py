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


# Main structured-output checks.

assert (
    "Research: \"Chennai airport status\""
    in answer
)

assert (
    "Key Findings"
    in answer
)

assert (
    "Conflicting Evidence"
    in answer
)

assert (
    "Sources"
    in answer
)


# Conflict information must be visible.

assert (
    "Sources disagree"
    in answer
)

assert (
    "resumed normally"
    in answer
)

assert (
    "remain disrupted"
    in answer
)


# Both sources must be preserved.

assert (
    "https://example.com/resumed"
    in answer
)

assert (
    "https://example.org/disrupted"
    in answer
)


print()
print(
    "CONFLICT SYNTHESIS PASSED"
)