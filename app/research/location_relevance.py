from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.research.models import Claim


_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def build_location_context(
    claim: Claim,
) -> str:

    parts = [
        claim.source_title,
        claim.statement,
        claim.source_url,
    ]

    return " ".join(
        part
        for part in parts
        if part
    )


def calculate_location_relevance(
    location: str,
    claim: Claim,
) -> float:

    claim_context = build_location_context(
        claim
    )

    embeddings = _model.encode(
        [
            location,
            claim_context,
        ]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]],
    )[0][0]

    return float(similarity)


def is_location_relevant(
    location: str,
    claim: Claim,
    threshold: float = 0.35,
) -> bool:

    score = calculate_location_relevance(
        location,
        claim,
    )

    return score >= threshold