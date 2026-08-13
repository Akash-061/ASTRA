from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


# --------------------------------------------------
# Turn 1
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="research recent issues in Chennai"
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
    == "Chennai"
)

assert (
    action.parameters["timeframe"]
    == "recent"
)


# --------------------------------------------------
# Turn 2
# --------------------------------------------------

response = orchestrator.handle(
    UserRequest(
        text="what about Bangalore?"
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
    == "Bangalore"
)

assert (
    action.parameters["timeframe"]
    == "recent"
)


# --------------------------------------------------
# Turn 3
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

assert len(history) == 3

assert (
    history[0].parameters["location"]
    == "Chennai"
)

assert (
    history[1].parameters["location"]
    == "Bangalore"
)

assert (
    history[2].parameters["location"]
    == "Mumbai"
)


assert (
    orchestrator.context.get_last_action()
    == history[-1]
)


print()
print("CONTEXT CHAIN PASSED")
print()

for index, action in enumerate(
    history,
    start=1,
):

    print(
        f"Turn {index}: "
        f"{action.parameters}"
    )