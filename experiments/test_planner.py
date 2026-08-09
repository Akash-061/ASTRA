from app.core.planner import create_plan


plan = create_plan(
    "open Chrome"
)

assert plan.intent == "open"

assert len(
    plan.actions
) == 1

assert (
    plan.actions[0].name
    == "open"
)

assert (
    plan.actions[0].parameters["command"]
    == "open Chrome"
)

print("PLANNER PASSED")