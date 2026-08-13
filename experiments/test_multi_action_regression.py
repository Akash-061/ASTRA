from app.core.planner import create_plan


# A normal research command should
# remain a single action.

plan = create_plan(
    "research AI and open source security tools"
)


assert len(plan.actions) == 1

assert (
    plan.actions[0].name
    == "research"
)


print()
print("MULTI-ACTION REGRESSION PASSED")
print()

print(
    "Intent:",
    plan.intent,
)

print(
    "Actions:",
    len(plan.actions),
)