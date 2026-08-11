from app.core.models import TaskPlan
from app.core.understanding import understand_command


def create_plan(
    command: str,
) -> TaskPlan:

    action = understand_command(
        command
    )

    return TaskPlan(
        intent=action.name,
        actions=[action],
    )