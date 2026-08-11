from app.core.models import Action
from app.research.adapter import (
    action_to_research_request,
)


action = Action(
    name="research",
    parameters={
        "topic": "issues",
        "location": "Chennai",
        "timeframe": "recent",
        "command": "recent issues in Chennai",
    },
)


request = action_to_research_request(
    action
)


assert request.topic == "issues"

assert request.location == "Chennai"

assert request.timeframe == "recent"

assert (
    request.original_query
    == "recent issues in Chennai"
)


print("RESEARCH ADAPTER PASSED")