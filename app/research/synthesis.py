from app.research.models import EvidenceGroup


def confidence_label(
    confidence: float,
) -> str:

    if confidence >= 0.75:
        return "High"

    if confidence >= 0.50:
        return "Moderate"

    if confidence >= 0.30:
        return "Low"

    return "Very Low"


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

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    lines.append(
        f'Research: "{query}"'
    )

    lines.append("")

    lines.append(
        "Key Findings"
    )

    lines.append(
        "------------"
    )

    lines.append("")

    # --------------------------------------------------
    # Findings
    # --------------------------------------------------

    for index, group in enumerate(
        selected_groups,
        start=1,
    ):

        lines.append(
            f"{index}. "
            f"{group.representative_claim}"
        )

        label = confidence_label(
            group.confidence
        )

        lines.append(
            f"   Confidence: "
            f"{label} "
            f"({group.confidence:.0%})"
        )

        lines.append(
            f"   Independent sources: "
            f"{len(group.domains)}"
        )

        lines.append(
            f"   Supporting claims: "
            f"{len(group.claims)}"
        )

        lines.append("")

    # --------------------------------------------------
    # Conflicting evidence
    # --------------------------------------------------

    conflicting_groups = [
        group
        for group in selected_groups
        if group.has_conflict
    ]

    if conflicting_groups:

        lines.append(
            "Conflicting Evidence"
        )

        lines.append(
            "--------------------"
        )

        lines.append("")

        for index, group in enumerate(
            conflicting_groups,
            start=1,
        ):

            lines.append(
                f"{index}. "
                f"{group.representative_claim}"
            )

            lines.append(
                "   ⚠️ Sources disagree "
                "on this point."
            )

            if group.conflicting_claims:

                lines.append(
                    "   Conflicting claims:"
                )

                for claim in (
                    group.conflicting_claims
                ):

                    lines.append(
                        f"   - "
                        f"{claim.statement}"
                    )

            lines.append("")

    # --------------------------------------------------
    # Sources
    # --------------------------------------------------

    lines.append(
        "Sources"
    )

    lines.append(
        "-------"
    )

    lines.append("")

    source_index = 1
    seen_sources = set()

    for group in selected_groups:

        for source in group.sources:

            if source in seen_sources:
                continue

            seen_sources.add(
                source
            )

            lines.append(
                f"[{source_index}] "
                f"{source}"
            )

            source_index += 1

    return "\n".join(
        lines
    ).strip()