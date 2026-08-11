from app.core.capability import Capability
from app.core.models import Action, ExecutionResult


class TestCapability(Capability):

    def execute(
        self,
        action: Action,
    ) -> ExecutionResult:

        return ExecutionResult(
            success=True,
            message="Test capability executed.",
            data={
                "command": action.parameters.get(
                    "command",
                    "",
                )
            },
        )


capability = TestCapability()

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
    == "Test capability executed."
)

assert (
    result.data["command"]
    == "hello ASTRA"
)


print("CAPABILITY CONTRACT PASSED")