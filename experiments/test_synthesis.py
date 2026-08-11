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
            "Tokyo residents reported "
            "recent transportation disruptions."
        ),
        claims=[
            Claim(
                statement=(
                    "Tokyo residents reported "
                    "recent transportation disruptions."
                ),
                sources=[
                    "https://example.com/transport"
                ],
                source_title="Tokyo transport report",
                source_url=(
                    "https://example.com/transport"
                ),
            )
        ],
        sources=[
            "https://example.com/transport"
        ],
        domains=[
            "example.com"
        ],
        confidence=0.40,
    ),
    EvidenceGroup(
        representative_claim=(
            "Several independent reports described "
            "major civic disruptions in Tokyo."
        ),
        claims=[
            Claim(
                statement=(
                    "Several independent reports described "
                    "major civic disruptions in Tokyo."
                ),
                sources=[
                    "https://news.example.com/tokyo"
                ],
                source_title="Tokyo civic report",
                source_url=(
                    "https://news.example.com/tokyo"
                ),
            )
        ],
        sources=[
            "https://news.example.com/tokyo"
        ],
        domains=[
            "news.example.com",
            "example.org",
            "example.net",
        ],
        confidence=0.85,
    ),
]


answer = synthesize_answer(
    "recent issues in Tokyo",
    groups,
)


assert (
    "recent issues in Tokyo"
    in answer
)

assert (
    "major civic disruptions"
    in answer
)

assert (
    "Confidence: 85%"
    in answer
)

assert (
    "news.example.com"
    in answer
)

print("SYNTHESIS PASSED")