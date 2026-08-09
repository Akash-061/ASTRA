from app.core.executor import Executor
from app.core.models import Action
from app.core.router import CAPABILITIES


def fake_capability(
    command: str,
):

    return {
        "command": command,
        "executed": True,
    }


original = CAPABILITIES.get("test")


CAPABILITIES["test"] = fake_capability


executor = Executor()

action = Action(
    name="test",
    parameters={
        "command": "hello ASTRA",
    },
)

result = executor.execute(
    action
)


assert result.success is True

assert (
    result.data["result"]["command"]
    == "hello ASTRA"
)

assert (
    result.data["result"]["executed"]
    is True
)


CAPABILITIES.pop("test")


if original is not None:
    CAPABILITIES["test"] = original


print("EXECUTOR PASSED")