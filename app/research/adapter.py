from app.core.models import Action
from app.research.request import ResearchRequest


def action_to_research_request(
    action: Action,
) -> ResearchRequest:

    parameters = action.parameters

    return ResearchRequest(
        topic=parameters.get(
            "topic",
            parameters.get(
                "command",
                "",
            ),
        ),
        location=parameters.get(
            "location"
        ),
        timeframe=parameters.get(
            "timeframe"
        ),
        scope=parameters.get(
            "scope"
        ),
        original_query=parameters.get(
            "command",
            "",
        ),
    )