from app.core.capabilities import FunctionCapability
from app.core.models import Action


def fake_search(
    topic: str,
    location: str,
):

    return {
        "success": True,
        "message": (
            f"Searching for {topic} "
            f"in {location}."
        ),
        "data": {
            "topic": topic,
            "location": location,
        },
    }


capability = FunctionCapability(
    fake_search
)


action = Action(
    name="search",
    parameters={
        "topic": "latest AI news",
        "location": "Tokyo",
    },
)


result = capability.execute(
    action
)


assert result.success is True

assert (
    result.message
    == "Searching for latest AI news in Tokyo."
)

assert (
    result.data["topic"]
    == "latest AI news"
)

assert (
    result.data["location"]
    == "Tokyo"
)


print("PARAMETER CAPABILITY PASSED")