from app.core.context_resolver import resolve_context
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
        command
    )

    action = resolve_context(
        action,
        previous_action,
    )

    return TaskPlan(
        intent=action.name,
        actions=[action],
    )