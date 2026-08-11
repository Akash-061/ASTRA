import app.research.engine as engine

from app.research.request import ResearchRequest
from app.research.models import (
    SearchResult,
    Claim,
    EvidenceGroup,
)


# --------------------------------------------------
# Mock search
# --------------------------------------------------

engine.search_web = lambda query: [
    SearchResult(
        title="Tokyo civic report",
        url="https://example.com/tokyo",
        snippet=(
            "Tokyo residents reported "
            "recent transportation disruptions."
        ),
    ),
]


# --------------------------------------------------
# Mock claim extraction
# --------------------------------------------------

engine.extract_claims = lambda results: [
    Claim(
        statement=(
            "Tokyo residents reported "
            "recent transportation disruptions."
        ),
        source_title="Tokyo civic report",
        source_url="https://example.com/tokyo",
        sources=[
            "https://example.com/tokyo"
        ],
    ),
]


# --------------------------------------------------
# Mock relevance filtering
# --------------------------------------------------

engine.is_relevant = (
    lambda query, claim: True
)


# --------------------------------------------------
# Mock verification
# --------------------------------------------------

engine.verify_claims = lambda claims: [
    EvidenceGroup(
        representative_claim=(
            "Tokyo residents reported "
            "recent transportation disruptions."
        ),
        claims=claims,
        sources=[
            "https://example.com/tokyo"
        ],
        domains=[
            "example.com"
        ],
        confidence=0.80,
    )
]


# --------------------------------------------------
# Research request
# --------------------------------------------------

request = ResearchRequest(
    topic="issues",
    location="Tokyo",
    timeframe="recent",
)


# --------------------------------------------------
# Run research engine
# --------------------------------------------------

result = engine.run_research(
    request
)


# --------------------------------------------------
# Assertions
# --------------------------------------------------

assert result["success"] is True


assert (
    result["data"]["query"]
    == "recent issues in Tokyo"
)


assert (
    result["data"]["sources"]
    == 1
)


assert (
    result["data"]["claims"]
    == 1
)


assert (
    result["data"]["relevant_claims"]
    == 1
)


assert (
    len(
        result["data"]["evidence_groups"]
    )
    == 1
)


# --------------------------------------------------
# Verify synthesized answer
# --------------------------------------------------

assert (
    "recent issues in Tokyo"
    in result["message"]
)


assert (
    "Tokyo residents reported"
    in result["message"]
)


assert (
    "transportation disruptions"
    in result["message"]
)


assert (
    "Confidence: 80%"
    in result["message"]
)


assert (
    "example.com"
    in result["message"]
)


print()
print("RESEARCH ENGINE RESPONSE")
print("--------------------------------")
print(result["message"])
print("--------------------------------")
print()
print("RESEARCH ENGINE PASSED")