from app.core.models import Action
from app.core.planner import create_plan


previous_action = Action(
    name="research",
    parameters={
        "command": "research recent issues in Chennai",
        "topic": "issues",
        "location": "Chennai",
        "timeframe": "recent",
    },
)


plan = create_plan(
    "what about Bangalore?",
    previous_action=previous_action,
)


assert plan.intent == "research"

assert len(plan.actions) == 1


action = plan.actions[0]


assert action.name == "research"

assert (
    action.parameters["topic"]
    == "issues"
)

assert (
    action.parameters["location"]
    == "Bangalore"
)

assert (
    action.parameters["timeframe"]
    == "recent"
)


print()
print("PLANNER CONTEXT PASSED")
print()
print(
    action.parameters
)
normal_plan = create_plan(
    "open Chrome",
    previous_action=previous_action,
)


assert normal_plan.intent == "open"

assert (
    normal_plan.actions[0].name
    == "open"
)

assert (
    normal_plan.actions[0].parameters["application"]
    == "Chrome"
)


print(
    "NORMAL PLANNER CONTEXT PASSED"
)