from app.research.request import ResearchRequest


def build_research_query(
    request: ResearchRequest,
) -> str:

    parts = []

    if request.timeframe:

        parts.append(
            request.timeframe
        )

    if request.topic:

        parts.append(
            request.topic
        )

    if request.location:

        parts.append(
            f"in {request.location}"
        )

    return " ".join(parts).strip()