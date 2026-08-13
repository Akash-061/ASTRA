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

        return ExecutionResult(
            success=True,
            message=(
                f"Executed {action.name}"
            ),
        )


executor = FakeExecutor()

orchestrator = Orchestrator(
    executor=executor
)


response = orchestrator.handle(
    UserRequest(
        text="open Chrome and open Notepad"
    )
)


assert response.success is True


# --------------------------------------------------
# Both actions must execute
# --------------------------------------------------

assert len(executor.actions) == 2


# --------------------------------------------------
# Action 1
# --------------------------------------------------

assert (
    executor.actions[0].name
    == "open"
)

assert (
    executor.actions[0].parameters[
        "application"
    ].lower()
    == "chrome"
)


# --------------------------------------------------
# Action 2
# --------------------------------------------------

assert (
    executor.actions[1].name
    == "open"
)

assert (
    executor.actions[1].parameters[
        "application"
    ].lower()
    == "notepad"
)


print()
print("MULTI-ACTION EXECUTION PASSED")
print()

for index, action in enumerate(
    executor.actions,
    start=1,
):

    print(
        f"Action {index}: "
        f"{action.parameters['application']}"
    )