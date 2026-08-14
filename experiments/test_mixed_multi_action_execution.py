from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


response = orchestrator.handle(
    UserRequest(
        text="open Chrome and tell me the time"
    )
)


# --------------------------------------------------
# Overall result
# --------------------------------------------------

assert response.success is True


# --------------------------------------------------
# Verify both actions were recorded
# --------------------------------------------------

history = (
    orchestrator.context.get_action_history()
)

assert len(history) == 2


# --------------------------------------------------
# Action 1
# --------------------------------------------------

first_action = history[0]

assert (
    first_action.name
    == "open"
)

assert (
    first_action.parameters[
        "application"
    ].lower()
    == "chrome"
)


# --------------------------------------------------
# Action 2
# --------------------------------------------------

second_action = history[1]

assert (
    second_action.name
    == "system"
)

assert (
    second_action.parameters[
        "command"
    ]
    == "time"
)


print()
print("MIXED MULTI-ACTION EXECUTION PASSED")
print()

for index, action in enumerate(
    history,
    start=1,
):

    print(
        f"Action {index}: "
        f"{action.name} - "
        f"{action.parameters}"
    )