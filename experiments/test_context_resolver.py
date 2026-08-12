from app.core.context_resolver import resolve_context
from app.core.models import Action


previous_action = Action(
    name="research",
    parameters={
        "command": "research recent issues in Chennai",
        "topic": "issues",
        "location": "Chennai",
        "timeframe": "recent",
    },
)


new_action = Action(
    name="unknown",
    parameters={
        "command": "what about Bangalore?",
    },
)


resolved = resolve_context(
    new_action,
    previous_action,
)


assert resolved.name == "research"

assert (
    resolved.parameters["topic"]
    == "issues"
)

assert (
    resolved.parameters["location"]
    == "Bangalore"
)

assert (
    resolved.parameters["timeframe"]
    == "recent"
)


print()
print(
    "CONTEXT RESOLVER PASSED"
)
print(
    resolved.parameters
)