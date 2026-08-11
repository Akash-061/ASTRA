from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.research.models import Claim


_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


ISSUE_CATEGORIES = {
    "power": (
        "power outages, electricity failures, "
        "blackouts, electrical supply problems"
    ),

    "civic": (
        "civic problems, damaged public infrastructure, "
        "municipal service problems, sanitation, "
        "water supply, garbage, street maintenance"
    ),

    "traffic": (
        "traffic congestion, road problems, "
        "parking shortages, transportation disruptions, "
        "commuting problems"
    ),

    "crime": (
        "crime, criminal activity, theft, robbery, "
        "assault, violence, shootings, arrests"
    ),

    "public_safety": (
        "public safety problems, accidents, hazards, "
        "dangerous conditions, emergencies"
    ),

    "health": (
        "public health problems, disease outbreaks, "
        "hospital problems, healthcare problems, "
        "medical emergencies affecting communities"
    ),

    "environment": (
        "environmental problems, pollution, flooding, "
        "wildfires, extreme weather, ecological damage"
    ),

    "housing": (
        "housing problems, homelessness, rent problems, "
        "housing shortages, unsafe housing"
    ),

    "education": (
        "education problems, school closures, "
        "school safety, problems affecting schools "
        "or students"
    ),
}


def build_claim_context(
    claim: Claim,
) -> str:

    parts = [
        claim.source_title,
        claim.statement,
    ]

    return " ".join(
        part
        for part in parts
        if part
    )


def calculate_category_scores(
    claim: Claim,
) -> dict[str, float]:

    claim_context = build_claim_context(
        claim
    )

    categories = list(
        ISSUE_CATEGORIES.keys()
    )

    category_descriptions = [
        ISSUE_CATEGORIES[category]
        for category in categories
    ]

    embeddings = _model.encode(
        [
            claim_context,
            *category_descriptions,
        ]
    )

    claim_embedding = embeddings[0]

    category_embeddings = embeddings[1:]

    similarities = cosine_similarity(
        [claim_embedding],
        category_embeddings,
    )[0]

    return {
        category: float(score)
        for category, score in zip(
            categories,
            similarities,
        )
    }


def calculate_issue_relevance(
    claim: Claim,
) -> float:

    scores = calculate_category_scores(
        claim
    )

    if not scores:
        return 0.0

    return max(
        scores.values()
    )


def is_issue(
    claim: Claim,
    threshold: float = 0.40,
) -> bool:

    score = calculate_issue_relevance(
        claim
    )

    return score >= threshold