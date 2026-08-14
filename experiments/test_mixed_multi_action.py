from app.core.planner import create_plan


plan = create_plan(
    "open Chrome and tell me the time"
)


# --------------------------------------------------
# Plan structure
# --------------------------------------------------

assert (
    plan.intent
    == "multi_action"
)

assert len(plan.actions) == 2


# --------------------------------------------------
# Action 1: Open Chrome
# --------------------------------------------------

first_action = plan.actions[0]

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
# Diagnostic output
# --------------------------------------------------

print()
print("Actual plan:")
print("Intent:", plan.intent)

for index, action in enumerate(
    plan.actions,
    start=1,
):
    print(
        f"Action {index}: "
        f"{action.name} - "
        f"{action.parameters}"
    )

print()


# --------------------------------------------------
# Action 2: Get time
# --------------------------------------------------

second_action = plan.actions[1]

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
print("MIXED MULTI-ACTION PLANNER PASSED")
print()