from app.core.planner import create_plan


plan = create_plan(
    "open Chrome and open Notepad and open Calculator"
)


assert (
    plan.intent
    == "multi_action"
)

assert len(plan.actions) == 3


expected_applications = [
    "chrome",
    "notepad",
    "calculator",
]


for action, expected in zip(
    plan.actions,
    expected_applications,
):

    assert action.name == "open"

    assert (
        action.parameters[
            "application"
        ].lower()
        == expected
    )


print()
print("THREE-ACTION PLANNER PASSED")
print()

for index, action in enumerate(
    plan.actions,
    start=1,
):

    print(
        f"Action {index}: "
        f"{action.name} - "
        f"{action.parameters['application']}"
    )