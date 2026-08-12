from app.core.context import ConversationContext
from app.core.models import Action


context = ConversationContext()


# --------------------------------------------------
# Message history
# --------------------------------------------------

context.add_message(
    "Hello ASTRA"
)

context.add_message(
    "Open Chrome"
)

context.add_message(
    "Search for MCA courses"
)


recent = context.get_recent()


assert len(recent) == 3

assert (
    recent[0]
    == "Hello ASTRA"
)

assert (
    recent[-1]
    == "Search for MCA courses"
)


# --------------------------------------------------
# Last action
# --------------------------------------------------

action = Action(
    name="research",
    parameters={
        "topic": "issues",
        "location": "Chennai",
        "timeframe": "recent",
    },
)


context.set_last_action(
    action
)


last_action = (
    context.get_last_action()
)


assert last_action is not None

assert (
    last_action.name
    == "research"
)

assert (
    last_action.parameters["topic"]
    == "issues"
)

assert (
    last_action.parameters["location"]
    == "Chennai"
)

assert (
    last_action.parameters["timeframe"]
    == "recent"
)


# --------------------------------------------------
# Clear
# --------------------------------------------------

context.clear()


assert (
    context.get_recent()
    == []
)

assert (
    context.get_last_action()
    is None
)


print(
    "CONTEXT PASSED"
)