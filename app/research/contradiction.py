from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.research.models import Claim


_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


CONTRADICTION_MARKERS = [
    ("is", "is not"),
    ("are", "are not"),
    ("was", "was not"),
    ("were", "were not"),
    ("has", "has not"),
    ("have", "have not"),
    ("can", "cannot"),
    ("will", "will not"),
    ("did", "did not"),

    ("reported", "denied"),
    ("confirmed", "denied"),

    ("resumed", "remain"),
    ("resumed", "remains"),
    ("resumed", "disrupted"),
    ("resume", "remain"),
    ("resume", "remains"),
    ("resume", "disrupted"),

    ("open", "closed"),

    ("increased", "decreased"),
    ("rose", "fell"),

    ("safe", "unsafe"),

    ("working", "not working"),

    ("available", "unavailable"),
]


def calculate_semantic_similarity(
    text_a: str,
    text_b: str,
) -> float:

    embeddings = _model.encode(
        [
            text_a,
            text_b,
        ]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]],
    )[0][0]

    return float(similarity)


def contains_contradiction_marker(
    text_a: str,
    text_b: str,
) -> bool:

    lowered_a = text_a.lower()
    lowered_b = text_b.lower()

    for positive, negative in (
        CONTRADICTION_MARKERS
    ):

        if (
            positive in lowered_a
            and negative in lowered_b
        ):
            return True

        if (
            negative in lowered_a
            and positive in lowered_b
        ):
            return True

    return False


def calculate_contradiction_score(
    claim_a: Claim,
    claim_b: Claim,
) -> float:

    similarity = (
        calculate_semantic_similarity(
            claim_a.statement,
            claim_b.statement,
        )
    )

    if not contains_contradiction_marker(
        claim_a.statement,
        claim_b.statement,
    ):
        return 0.0

    return similarity


def are_contradictory(
    claim_a: Claim,
    claim_b: Claim,
    threshold: float = 0.45,
) -> bool:

    score = (
        calculate_contradiction_score(
            claim_a,
            claim_b,
        )
    )

    return score >= threshold