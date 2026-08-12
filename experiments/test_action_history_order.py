from app.core.models import (
    ExecutionResult,
    UserRequest,
)
from app.core.orchestrator import Orchestrator


class FakeExecutor:

    def __init__(self):
        self.actions = []

    def execute(self, action):

        self.actions.append(action)

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


commands = [
    "open Chrome",
    "open Notepad",
]


for command in commands:

    response = orchestrator.handle(
        UserRequest(
            text=command
        )
    )

    assert response.success is True


history = (
    orchestrator.context.get_action_history()
)


assert len(history) == 2


assert history[0].name == "open"

assert (
    history[0].parameters["application"]
    == "Chrome"
)


assert history[1].name == "open"

assert (
    history[1].parameters["application"]
    == "Notepad"
)


assert (
    orchestrator.context.get_last_action()
    == history[-1]
)


assert len(executor.actions) == 2


print()
print("ACTION HISTORY ORDER PASSED")