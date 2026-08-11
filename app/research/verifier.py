from app.research.models import (
    Claim,
    EvidenceGroup,
)

from app.research.matcher import (
    group_similar_claims,
)

from app.research.source import (
    get_domain,
)

from app.research.source_quality import (
    calculate_source_quality,
)

from app.research.contradiction import (
    are_contradictory,
)


def calculate_domain_confidence(
    domain_count: int,
) -> float:

    if domain_count == 1:
        return 0.40

    if domain_count == 2:
        return 0.65

    if domain_count >= 3:
        return 0.85

    return 0.0


def calculate_quality_bonus(
    sources: list[str],
) -> float:

    if not sources:
        return 0.0

    scores = []

    for source in sources:

        score = calculate_source_quality(
            source
        )

        scores.append(score)

    if not scores:
        return 0.0

    average_quality = (
        sum(scores)
        / len(scores)
    )

    if average_quality <= 0.50:
        return 0.0

    bonus = (
        average_quality
        - 0.50
    ) * 0.20

    return min(
        bonus,
        0.10,
    )


def calculate_evidence_confidence(
    domain_count: int,
    sources: list[str],
    has_conflict: bool = False,
) -> float:

    base_confidence = (
        calculate_domain_confidence(
            domain_count
        )
    )

    quality_bonus = (
        calculate_quality_bonus(
            sources
        )
    )

    confidence = (
        base_confidence
        + quality_bonus
    )

    if has_conflict:

        confidence *= 0.50

    return min(
        confidence,
        1.0,
    )


def find_conflicting_claims(
    claims: list[Claim],
) -> list[Claim]:

    conflicting_claims = []

    for index, claim_a in enumerate(
        claims
    ):

        for claim_b in claims[
            index + 1:
        ]:

            if are_contradictory(
                claim_a,
                claim_b,
            ):

                if (
                    claim_a
                    not in conflicting_claims
                ):
                    conflicting_claims.append(
                        claim_a
                    )

                if (
                    claim_b
                    not in conflicting_claims
                ):
                    conflicting_claims.append(
                        claim_b
                    )

    return conflicting_claims


def verify_claims(
    claims: list[Claim],
    similarity_threshold: float = 0.35,
) -> list[EvidenceGroup]:

    groups = group_similar_claims(
        claims,
        threshold=similarity_threshold,
    )

    evidence_groups = []

    for group in groups:

        if not group:
            continue

        representative_claim = (
            group[0].statement
        )

        sources = []
        domains = set()

        for claim in group:

            for source in claim.sources:

                if source not in sources:

                    sources.append(
                        source
                    )

                domain = get_domain(
                    source
                )

                if domain:

                    domains.add(
                        domain
                    )

        conflicting_claims = (
            find_conflicting_claims(
                group
            )
        )

        has_conflict = bool(
            conflicting_claims
        )

        domain_count = len(
            domains
        )

        confidence = (
            calculate_evidence_confidence(
                domain_count,
                sources,
                has_conflict,
            )
        )

        evidence_groups.append(
            EvidenceGroup(
                representative_claim=(
                    representative_claim
                ),
                claims=group,
                sources=sources,
                domains=sorted(
                    domains
                ),
                confidence=confidence,
                has_conflict=(
                    has_conflict
                ),
                conflicting_claims=(
                    conflicting_claims
                ),
            )
        )

    return evidence_groups