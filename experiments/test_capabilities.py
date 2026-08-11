from app.core.capabilities import FunctionCapability
from app.core.models import Action


def fake_function(command: str):

    return {
        "success": True,
        "message": "Fake capability executed.",
        "data": {
            "command": command,
        },
    }


capability = FunctionCapability(
    fake_function
)

action = Action(
    name="test",
    parameters={
        "command": "hello ASTRA",
    },
)

result = capability.execute(
    action
)


assert result.success is True

assert (
    result.message
    == "Fake capability executed."
)

assert (
    result.data["command"]
    == "hello ASTRA"
)


print("FUNCTION CAPABILITY PASSED")