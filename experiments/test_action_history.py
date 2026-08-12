from app.core.context import ConversationContext
from app.core.models import Action


context = ConversationContext()


first_action = Action(
    name="research",
    parameters={
        "topic": "AI developments",
        "location": "India",
    },
)


second_action = Action(
    name="research",
    parameters={
        "topic": "AI developments",
        "location": "Japan",
    },
)


context.set_last_action(
    first_action
)

context.add_action(
    first_action
)

context.set_last_action(
    second_action
)

context.add_action(
    second_action
)


history = context.get_action_history()


assert len(history) == 2

assert history[0].name == "research"

assert (
    history[0].parameters["location"]
    == "India"
)

assert history[1].name == "research"

assert (
    history[1].parameters["location"]
    == "Japan"
)


assert (
    context.get_last_action()
    == second_action
)


context.clear()


assert context.get_action_history() == []

assert context.get_last_action() is None


print()
print("ACTION HISTORY PASSED")