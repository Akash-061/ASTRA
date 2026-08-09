from app.core.intent import detect_intent
from app.core.models import Action, TaskPlan


def create_plan(
    command: str,
) -> TaskPlan:

    intent = detect_intent(
        command
    )

    action = Action(
        name=intent,
        parameters={
            "command": command,
        },
    )

    return TaskPlan(
        intent=intent,
        actions=[action],
    )