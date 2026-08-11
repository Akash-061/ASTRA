from app.research.models import EvidenceGroup


def synthesize_answer(
    query: str,
    evidence_groups: list[EvidenceGroup],
    max_groups: int = 8,
) -> str:

    if not evidence_groups:

        return (
            f"I couldn't find enough verified evidence "
            f"to answer: {query}"
        )

    # Strongest evidence first.
    ranked_groups = sorted(
        evidence_groups,
        key=lambda group: (
            group.confidence,
            len(group.domains),
            len(group.claims),
        ),
        reverse=True,
    )

    selected_groups = ranked_groups[
        :max_groups
    ]

    lines = []

    lines.append(
        f'Based on the available evidence for '
        f'"{query}":'
    )

    lines.append("")

    for index, group in enumerate(
        selected_groups,
        start=1,
    ):

        lines.append(
            f"{index}. "
            f"{group.representative_claim}"
        )

        lines.append(
            f"   Confidence: "
            f"{group.confidence:.0%}"
        )

        if group.has_conflict:

            lines.append(
                "   ⚠️ Conflict detected: "
                "sources disagree on this point."
            )

            if group.conflicting_claims:

                lines.append(
                    "   Conflicting evidence:"
                )

                for claim in (
                    group.conflicting_claims
                ):

                    lines.append(
                        f"   - {claim.statement}"
                    )

        if group.domains:

            lines.append(
                "   Independent sources: "
                + ", ".join(
                    group.domains
                )
            )

        if group.sources:

            lines.append(
                "   Sources:"
            )

            for source in group.sources:

                lines.append(
                    f"   - {source}"
                )

        lines.append("")

    return "\n".join(
        lines
    ).strip()