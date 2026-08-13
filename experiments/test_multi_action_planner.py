from app.core.planner import create_plan


plan = create_plan(
    "open Chrome and open Notepad"
)


assert (
    len(plan.actions)
    == 2
)


assert (
    plan.actions[0].name
    == "open"
)

assert (
    plan.actions[0].parameters[
        "application"
    ].lower()
    == "chrome"
)


assert (
    plan.actions[1].name
    == "open"
)

assert (
    plan.actions[1].parameters[
        "application"
    ].lower()
    == "notepad"
)


print()
print("MULTI-ACTION PLANNER PASSED")
print()

for index, action in enumerate(
    plan.actions,
    start=1,
):

    print(
        f"Action {index}: "
        f"{action.name} - "
        f"{action.parameters}"
    )