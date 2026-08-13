from app.core.models import (
    ExecutionResult,
    UserRequest,
)
from app.core.orchestrator import Orchestrator


class FakeExecutor:

    def __init__(self):
        self.actions = []

    def execute(
        self,
        action,
    ) -> ExecutionResult:

        self.actions.append(
            action
        )

        application = (
            action.parameters.get(
                "application",
                "",
            ).lower()
        )

        if application == "unknownapp":

            return ExecutionResult(
                success=False,
                message="Application not found.",
            )

        return ExecutionResult(
            success=True,
            message=(
                f"Opened {application}"
            ),
        )


executor = FakeExecutor()

orchestrator = Orchestrator(
    executor=executor
)


response = orchestrator.handle(
    UserRequest(
        text=(
            "open Chrome and "
            "open UnknownApp"
        )
    )
)


# Overall request must fail because
# one action failed.
assert response.success is False


# Both actions should have been attempted.
assert len(executor.actions) == 2


assert (
    executor.actions[0].parameters[
        "application"
    ].lower()
    == "chrome"
)

assert (
    executor.actions[1].parameters[
        "application"
    ].lower()
    == "unknownapp"
)


print()
print("MULTI-ACTION PARTIAL FAILURE PASSED")
print()

print(
    "Response:",
    response.message,
)