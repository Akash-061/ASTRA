from app.core.models import (
    Action,
    TaskPlan,
)
from app.core.understanding import (
    understand_command,
)


def create_plan(
    command: str,
    previous_action: Action | None = None,
) -> TaskPlan:

    action = understand_command(
        command,
        previous_action=previous_action,
    )

    return TaskPlan(
        intent=action.name,
        actions=[action],
    )