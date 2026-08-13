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


# --------------------------------------------------
# Turn 1 — Research
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="research recent issues in Chennai"
    )
)

assert response.success is True


# --------------------------------------------------
# Turn 2 — Research follow-up
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="what about Bangalore?"
    )
)

assert response.success is True


# --------------------------------------------------
# Turn 3 — Switch capability
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="open Chrome"
    )
)

assert response.success is True


# --------------------------------------------------
# Turn 4 — Return to research context
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="what about Mumbai?"
    )
)

assert response.success is True


action = (
    orchestrator.context.get_last_action()
)


assert action is not None

assert action.name == "research"

assert (
    action.parameters["topic"]
    == "issues"
)

assert (
    action.parameters["location"]
    == "Mumbai"
)

assert (
    action.parameters["timeframe"]
    == "recent"
)


# --------------------------------------------------
# Verify action history
# --------------------------------------------------

history = (
    orchestrator.context.get_action_history()
)


assert len(history) == 4

assert history[0].name == "research"

assert history[1].name == "research"

assert history[2].name == "open"

assert history[3].name == "research"


assert (
    history[3].parameters["location"]
    == "Mumbai"
)


print()
print("CONTEXT SWITCH PASSED")
print()

for index, action in enumerate(
    history,
    start=1,
):

    print(
        f"Turn {index}: "
        f"{action.name} → "
        f"{action.parameters}"
    )