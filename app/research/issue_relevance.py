from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.research.models import Claim


_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


ISSUE_CATEGORIES = {

    "civic": (
        "local civic problems affecting residents, "
        "municipal problems, public complaints, "
        "street infrastructure, garbage collection, "
        "street maintenance, public facilities"
    ),

    "infrastructure": (
        "infrastructure problems, damaged roads, "
        "damaged buildings, broken street infrastructure, "
        "construction problems, public infrastructure failures"
    ),

    "traffic": (
        "traffic congestion, road accidents, "
        "transportation problems, parking problems, "
        "traffic disruption, road safety"
    ),

    "power": (
        "electricity problems, power outages, "
        "power cuts, electrical failures, "
        "electricity supply disruptions"
    ),

    "water": (
        "water supply problems, water shortages, "
        "drinking water problems, contaminated water, "
        "water distribution failures"
    ),

    "drainage": (
        "stormwater drainage problems, flooding, "
        "blocked drains, sewage problems, "
        "waterlogging, drainage infrastructure"
    ),

    "pollution": (
        "air pollution, water pollution, "
        "chemical pollution, environmental contamination, "
        "bad smells, toxic emissions"
    ),

    "crime": (
        "crime, theft, robbery, assault, "
        "fraud, criminal activity, arrests"
    ),

    "public_safety": (
        "public safety problems, dangerous conditions, "
        "safety concerns affecting residents, "
        "accidents and hazards"
    ),

    "environment": (
        "environmental problems, environmental damage, "
        "ecological concerns, waste, pollution, "
        "damage to natural resources"
    ),

    "protest": (
        "public protests, demonstrations, strikes, "
        "residents protesting, public demands, "
        "community opposition"
    ),

    "government_services": (
        "government service failures, municipal services, "
        "public service problems, administrative failures, "
        "government response to local problems"
    ),
}


def calculate_category_scores(
    claim: Claim,
) -> dict[str, float]:

    claim_context = (
        f"{claim.source_title} "
        f"{claim.statement}"
    )

    texts = [
        claim_context,
        *ISSUE_CATEGORIES.values(),
    ]

    embeddings = _model.encode(
        texts
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
            ISSUE_CATEGORIES.keys(),
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
    threshold: float = 0.30,
) -> bool:

    score = calculate_issue_relevance(
        claim
    )

    return score >= threshold