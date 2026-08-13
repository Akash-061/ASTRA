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

        self.actions.append(action)

        return ExecutionResult(
            success=True,
            message=f"Executed {action.name}",
        )


executor = FakeExecutor()

orchestrator = Orchestrator(
    executor=executor
)


# --------------------------------------------------
# Establish research context
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="research recent issues in Chennai"
    )
)

assert response.success is True


first_action = (
    orchestrator.context.get_last_action()
)

assert first_action is not None

assert first_action.name == "research"

assert (
    first_action.parameters["topic"]
    == "issues"
)

assert (
    first_action.parameters["location"]
    == "Chennai"
)


# --------------------------------------------------
# Ambiguous follow-up
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="what about it?"
    )
)


# ASTRA must NOT silently create a
# research action from an ambiguous
# reference.
assert response.success is False


# The ambiguous request must not create
# another action-history entry.
history = (
    orchestrator.context.get_action_history()
)

assert len(history) == 1

assert history[0].name == "research"

assert (
    history[0].parameters["location"]
    == "Chennai"
)


# The last valid action remains the
# previous research action.
last_action = (
    orchestrator.context.get_last_action()
)

assert last_action is not None

assert last_action.name == "research"

assert (
    last_action.parameters["location"]
    == "Chennai"
)


print()
print("CONTEXT AMBIGUITY PASSED")
print()

print(
    "Response:",
    response.message,
)