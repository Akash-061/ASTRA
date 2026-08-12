from app.core.context_resolver import resolve_context
from app.core.models import Action


previous_action = Action(
    name="research",
    parameters={
        "command": "research recent AI developments in India",
        "topic": "AI developments",
        "location": "India",
        "timeframe": "recent",
    },
)


# New action only changes the location.
new_action = Action(
    name="unknown",
    parameters={
        "command": "what about Japan?",
        "location": "Japan",
    },
)


resolved = resolve_context(
    new_action,
    previous_action,
)


print()
print(
    "Resolved parameters:"
)

print(
    resolved.parameters
)


assert resolved.name == "research"

assert (
    resolved.parameters["topic"]
    == "AI developments"
)

assert (
    resolved.parameters["location"]
    == "Japan"
)

assert (
    resolved.parameters["timeframe"]
    == "recent"
)


print()
print(
    "PARAMETER INHERITANCE PASSED"
)