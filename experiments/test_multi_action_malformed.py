from app.core.planner import create_plan


commands = [
    "open Chrome and",
    "open Chrome,",
]


for command in commands:

    plan = create_plan(
        command
    )

    # Malformed commands must not
    # become multi-action plans.
    assert (
        plan.intent
        != "multi_action"
    )

    assert len(plan.actions) == 1


print()
print("MALFORMED MULTI-ACTION PASSED")
print()