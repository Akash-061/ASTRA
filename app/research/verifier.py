from app.research.models import Claim
from app.research.source import get_domain


def verify_claims(claims: list[Claim]) -> list[Claim]:

    groups = {}

    for claim in claims:

        normalized = claim.statement.strip().lower()

        if not normalized:
            continue

        if normalized not in groups:
            groups[normalized] = {
                "statement": claim.statement,
                "sources": [],
                "domains": set(),
            }

        for source in claim.sources:

            if source not in groups[normalized]["sources"]:

                groups[normalized]["sources"].append(source)

                domain = get_domain(source)

                if domain:
                    groups[normalized]["domains"].add(domain)

    verified_claims = []

    for data in groups.values():

        source_count = len(data["sources"])
        domain_count = len(data["domains"])

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
                statement=data["statement"],
                sources=data["sources"],
                confidence=confidence,
            )
        )

    return verified_claims