from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


# --------------------------------------------------
# First turn
# --------------------------------------------------

first_request = UserRequest(
    text="research recent issues in Chennai"
)


first_response = orchestrator.handle(
    first_request
)


assert first_response.success is True


first_action = (
    orchestrator.context.get_last_action()
)


assert first_action is not None

assert (
    first_action.name
    == "research"
)

assert (
    first_action.parameters["topic"]
    == "issues"
)

assert (
    first_action.parameters["location"]
    == "Chennai"
)

assert (
    first_action.parameters["timeframe"]
    == "recent"
)


# --------------------------------------------------
# Second turn
# --------------------------------------------------

second_request = UserRequest(
    text="what about Bangalore?"
)


second_response = orchestrator.handle(
    second_request
)


assert second_response.success is True


second_action = (
    orchestrator.context.get_last_action()
)


assert second_action is not None

assert (
    second_action.name
    == "research"
)

assert (
    second_action.parameters["topic"]
    == "issues"
)

assert (
    second_action.parameters["location"]
    == "Bangalore"
)

assert (
    second_action.parameters["timeframe"]
    == "recent"
)


# --------------------------------------------------
# Conversation history
# --------------------------------------------------

history = (
    orchestrator.context.get_recent()
)


assert (
    history
    == [
        "research recent issues in Chennai",
        "what about Bangalore?",
    ]
)


print()
print("MULTI-TURN CONTEXT PASSED")
print()
print(
    "First action:",
    first_action.parameters,
)
print(
    "Second action:",
    second_action.parameters,
)