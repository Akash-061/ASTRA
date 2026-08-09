from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.research.models import Claim


_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


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


def calculate_semantic_relevance(
    query: str,
    claim: Claim,
) -> float:

    claim_context = build_claim_context(
        claim
    )

    embeddings = _model.encode(
        [
            query,
            claim_context,
        ]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]],
    )[0][0]

    return float(similarity)


def is_semantically_relevant(
    query: str,
    claim: Claim,
    threshold: float = 0.35,
) -> bool:

    score = calculate_semantic_relevance(
        query,
        claim,
    )

    return score >= threshold