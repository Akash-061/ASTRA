from app.core.context_resolver import resolve_context
from app.core.models import (
    Action,
    TaskPlan,
)
from app.core.understanding import (
    understand_command,
)


def _split_open_commands(
    command: str,
) -> list[str] | None:

    parts = command.split(
        " and open "
    )

    if len(parts) < 2:
        return None

    commands = []

    for index, part in enumerate(parts):

        part = part.strip()

        if index > 0:
            part = (
                "open "
                + part
            )

        if not part.lower().startswith(
            "open "
        ):
            return None

        commands.append(part)

    return commands


def create_plan(
    command: str,
    previous_action: Action | None = None,
) -> TaskPlan:

    # --------------------------------------------------
    # Multi-action open commands
    # --------------------------------------------------

    commands = _split_open_commands(
        command
    )

    if commands:

        actions = []

        for single_command in commands:

            action = understand_command(
                single_command
            )

            if action.name != "open":
                return TaskPlan(
                    intent=action.name,
                    actions=[action],
                )

            actions.append(action)

        return TaskPlan(
            intent="multi_action",
            actions=actions,
        )

    # --------------------------------------------------
    # Single-action command
    # --------------------------------------------------

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