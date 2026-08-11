from app.core.planner import create_plan


plan = create_plan(
    "open Chrome"
)


assert plan.intent == "open"

assert len(
    plan.actions
) == 1


action = plan.actions[0]


assert action.name == "open"

assert (
    action.parameters["command"]
    == "open Chrome"
)

assert (
    action.parameters["application"]
    == "Chrome"
)


print("PLANNER PASSED")