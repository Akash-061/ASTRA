from app.research.models import Claim
from app.research.matcher import group_similar_claims
from app.research.source import get_domain


def verify_claims(
    claims: list[Claim],
    similarity_threshold: float = 0.35,
) -> list[Claim]:

    groups = group_similar_claims(
        claims,
        threshold=similarity_threshold,
    )

    verified_claims = []

    for group in groups:

        if not group:
            continue

        statement = group[0].statement

        sources = []
        domains = set()

        for claim in group:

            for source in claim.sources:

                if source not in sources:
                    sources.append(source)

                domain = get_domain(source)

                if domain:
                    domains.add(domain)

        domain_count = len(domains)

        if domain_count == 1:
            confidence = 0.40

        elif domain_count == 2:
            confidence = 0.65

        elif domain_count >= 3:
            confidence = 0.85

        else:
            confidence = 0.0

        verified_claims.append(
            Claim(
                statement=statement,
                sources=sources,
                confidence=confidence,
            )
        )

    return verified_claims