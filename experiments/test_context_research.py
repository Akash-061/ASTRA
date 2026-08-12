from app.core.models import Action
from app.core.understanding import understand_command


previous_action = Action(
    name="research",
    parameters={
        "command": "research recent issues in Chennai",
        "topic": "issues",
        "location": "Chennai",
        "timeframe": "recent",
    },
)


action = understand_command(
    "what about Bangalore?",
    previous_action=previous_action,
)


print(
    f"Action: {action.name}"
)

print(
    f"Parameters: {action.parameters}"
)


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


print(
    "CONTEXT RESEARCH PASSED"
)