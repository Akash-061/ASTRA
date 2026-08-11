from app.core.capabilities import FunctionCapability
from app.core.models import Action


def fake_action_function(
    action: Action,
):

    return {
        "success": True,
        "message": "Action received.",
        "data": {
            "name": action.name,
            "topic": action.parameters.get(
                "topic"
            ),
            "location": action.parameters.get(
                "location"
            ),
        },
    }


fake_action_function.accepts_action = True


capability = FunctionCapability(
    fake_action_function
)


action = Action(
    name="research",
    parameters={
        "topic": "AI",
        "location": "Tokyo",
    },
)


result = capability.execute(
    action
)


assert result.success is True

assert (
    result.data["name"]
    == "research"
)

assert (
    result.data["topic"]
    == "AI"
)

assert (
    result.data["location"]
    == "Tokyo"
)


print("ACTION CAPABILITY PASSED")