from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.research.models import Claim


def calculate_similarity(
    text_a: str,
    text_b: str,
) -> float:

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        [text_a, text_b]
    )

    similarity = cosine_similarity(vectors)[0][1]

    return float(similarity)


def are_similar(
    text_a: str,
    text_b: str,
    threshold: float = 0.35,
) -> bool:

    similarity = calculate_similarity(
        text_a,
        text_b,
    )

    return similarity >= threshold


def group_similar_claims(
    claims: list[Claim],
    threshold: float = 0.35,
) -> list[list[Claim]]:

    groups = []

    for claim in claims:

        placed = False

        for group in groups:

            representative = group[0]

            if are_similar(
                claim.statement,
                representative.statement,
                threshold,
            ):

                group.append(claim)
                placed = True
                break

        if not placed:

            groups.append([claim])

    return groups