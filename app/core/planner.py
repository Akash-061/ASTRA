import re

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

    lowered = command.lower().strip()

    # Multi-action open commands must
    # begin with "open".
    if not lowered.startswith(
        "open "
    ):
        return None

    # Remove the first "open".
    applications_text = command[
        len("open "):
    ].strip()

    # Normalize:
    #
    # open Chrome then open Notepad
    #
    # into:
    #
    # Chrome and Notepad
    applications_text = re.sub(
        r"\bthen\s+open\b",
        "and",
        applications_text,
        flags=re.IGNORECASE,
    )

    # Normalize:
    #
    # Chrome and open Notepad
    #
    # into:
    #
    # Chrome and Notepad
    applications_text = re.sub(
        r"\band\s+open\b",
        "and",
        applications_text,
        flags=re.IGNORECASE,
    )

    # Normalize commas:
    #
    # Chrome, Notepad and Calculator
    #
    # into:
    #
    # Chrome and Notepad and Calculator
    applications_text = re.sub(
        r"\s*,\s*",
        " and ",
        applications_text,
    )

    # Split application names.
    parts = re.split(
        r"\s+and\s+",
        applications_text,
        flags=re.IGNORECASE,
    )

    # A multi-action command needs at
    # least two applications.
    if len(parts) < 2:
        return None

    commands = []

    for part in parts:

        application = part.strip()

        # Reject malformed commands such as:
        #
        # open Chrome and
        if not application:
            return None

        commands.append(
            f"open {application}"
        )

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

            # Safety check:
            # every split command must still
            # be understood as an open action.
            if action.name != "open":

                return TaskPlan(
                    intent=action.name,
                    actions=[action],
                )

            actions.append(
                action
            )

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