from app.research.models import SearchResult, Claim


def extract_claims(
    results: list[SearchResult],
) -> list[Claim]:

    claims = []

    for result in results:

        statement = result.snippet.strip()

        if not statement:
            continue

        claim = Claim(
            statement=statement,
            sources=[result.url],
            confidence=0.0,
        )

        claims.append(claim)

    return claims