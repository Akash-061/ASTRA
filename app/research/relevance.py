from app.research.models import Claim
from app.research.semantic_relevance import (
    calculate_semantic_relevance,
)


def calculate_relevance(
    query: str,
    claim: Claim,
) -> float:

    semantic_score = calculate_semantic_relevance(
        query,
        claim,
    )

    return semantic_score


def is_relevant(
    query: str,
    claim: Claim,
    threshold: float = 0.35,
) -> bool:

    score = calculate_relevance(
        query,
        claim,
    )

    return score >= threshold