import re

from app.research.models import Claim
from app.research.request import ResearchRequest

from app.research.semantic_relevance import (
    calculate_semantic_relevance,
)

from app.research.location_relevance import (
    calculate_location_relevance,
)

from app.research.issue_relevance import (
    calculate_issue_relevance,
)


def tokenize(text: str) -> set[str]:

    return set(
        re.findall(
            r"\b[a-z0-9]+\b",
            text.lower(),
        )
    )


def calculate_text_similarity(
    text_a: str,
    text_b: str,
) -> float:

    tokens_a = tokenize(text_a)
    tokens_b = tokenize(text_b)

    if not tokens_a or not tokens_b:
        return 0.0

    intersection = (
        tokens_a & tokens_b
    )

    union = (
        tokens_a | tokens_b
    )

    return (
        len(intersection)
        / len(union)
    )


def calculate_relevance(
    query: str,
    claim: Claim,
) -> float:

    semantic_score = (
        calculate_semantic_relevance(
            query,
            claim,
        )
    )

    title_score = (
        calculate_text_similarity(
            query,
            claim.source_title,
        )
    )

    url_score = (
        calculate_text_similarity(
            query,
            claim.source_url,
        )
    )

    return float(
        semantic_score * 0.60
        + title_score * 0.25
        + url_score * 0.15
    )


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


def calculate_contextual_relevance(
    request: ResearchRequest,
    claim: Claim,
) -> dict[str, float]:

    query = request.original_query

    if not query:

        parts = []

        if request.timeframe:
            parts.append(
                request.timeframe
            )

        if request.topic:
            parts.append(
                request.topic
            )

        if request.location:
            parts.append(
                f"in {request.location}"
            )

        query = " ".join(
            parts
        ).strip()

    semantic_score = (
        calculate_semantic_relevance(
            query,
            claim,
        )
    )

    title_score = (
        calculate_text_similarity(
            query,
            claim.source_title,
        )
    )

    url_score = (
        calculate_text_similarity(
            query,
            claim.source_url,
        )
    )

    location_score = 0.0

    if request.location:

        location_score = (
            calculate_location_relevance(
                request.location,
                claim,
            )
        )

    issue_score = (
        calculate_issue_relevance(
            claim
        )
    )

    final_score = (
        semantic_score * 0.40
        + title_score * 0.15
        + url_score * 0.10
        + location_score * 0.25
        + issue_score * 0.10
    )

    return {
        "semantic": float(
            semantic_score
        ),
        "title": float(
            title_score
        ),
        "url": float(
            url_score
        ),
        "location": float(
            location_score
        ),
        "issue": float(
            issue_score
        ),
        "final": float(
            final_score
        ),
    }


def is_contextually_relevant(
    request: ResearchRequest,
    claim: Claim,
    location_threshold: float = 0.30,
    issue_threshold: float = 0.35,
) -> bool:

    scores = (
        calculate_contextual_relevance(
            request,
            claim,
        )
    )

    if request.location:

        if (
            scores["location"]
            < location_threshold
        ):
            return False

    if request.topic:

        if (
            request.topic.lower()
            == "issues"
        ):

            if (
                scores["issue"]
                < issue_threshold
            ):
                return False

    return True