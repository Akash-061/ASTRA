from app.research.models import (
    Claim,
    EvidenceGroup,
)

from app.research.synthesis import (
    synthesize_answer,
)


groups = [

    EvidenceGroup(
        representative_claim=(
            "Recurring power outages "
            "affected residents in Adyar."
        ),
        claims=[
            Claim(
                statement=(
                    "Recurring power outages "
                    "affected residents in Adyar."
                )
            )
        ],
        sources=[
            "https://example.com/power",
            "https://example.org/power",
        ],
        domains=[
            "example.com",
            "example.org",
        ],
        confidence=0.80,
    ),

    EvidenceGroup(
        representative_claim=(
            "Parking shortages and traffic "
            "congestion affected Anna Nagar."
        ),
        claims=[
            Claim(
                statement=(
                    "Parking shortages and traffic "
                    "congestion affected Anna Nagar."
                )
            )
        ],
        sources=[
            "https://example.net/traffic",
        ],
        domains=[
            "example.net",
        ],
        confidence=0.40,
    ),

    EvidenceGroup(
        representative_claim=(
            "Reports disagreed about the status "
            "of a Chennai airport disruption."
        ),
        claims=[
            Claim(
                statement=(
                    "Chennai airport operations "
                    "resumed normally."
                )
            ),
            Claim(
                statement=(
                    "Chennai airport operations "
                    "remain disrupted."
                )
            ),
        ],
        sources=[
            "https://example.com/airport",
            "https://example.org/airport",
        ],
        domains=[
            "example.com",
            "example.org",
        ],
        confidence=0.30,
        has_conflict=True,
        conflicting_claims=[
            Claim(
                statement=(
                    "Chennai airport operations "
                    "resumed normally."
                )
            ),
            Claim(
                statement=(
                    "Chennai airport operations "
                    "remain disrupted."
                )
            ),
        ],
    ),
]


answer = synthesize_answer(
    "recent issues in Chennai",
    groups,
)


print()
print("================================")
print("STRUCTURED SYNTHESIS TEST")
print("================================")
print()
print(answer)
print()


assert "recent issues in Chennai" in answer

assert (
    "Key Findings"
    in answer
)

assert (
    "Confidence"
    in answer
)

assert (
    "Independent sources"
    in answer
)

assert (
    "Conflicting Evidence"
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

assert (
    "Sources"
    in answer
)


print(
    "STRUCTURED SYNTHESIS PASSED"
)