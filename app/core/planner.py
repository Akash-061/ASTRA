import re

from app.core.context_resolver import resolve_context
from app.core.models import (
    Action,
    TaskPlan,
)
from app.core.understanding import (
    understand_command,
)


# Applications currently supported by ASTRA's
# natural multi-open command handling.
KNOWN_APPLICATIONS = {
    "chrome",
    "google chrome",
    "notepad",
    "calculator",
}


def _normalize_application(
    application: str,
) -> str:

    return (
        application.lower()
        .strip()
    )


def _is_known_application(
    application: str,
) -> bool:

    normalized = _normalize_application(
        application
    )

    return (
        normalized in KNOWN_APPLICATIONS
    )


def _split_open_commands(
    command: str,
) -> list[str] | None:

    lowered = command.lower().strip()

    # Only commands beginning with "open"
    # can use the multi-open splitter.
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
    # Chrome then open Notepad
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

    # Must contain at least two applications.
    if len(parts) < 2:
        return None

    commands = []

    for part in parts:

        application = part.strip()

        # Reject malformed commands.
        if not application:
            return None

        # IMPORTANT:
        #
        # Only known application names can be
        # converted into additional open actions.
        #
        # This prevents:
        #
        # open Chrome and tell me the time
        #
        # from becoming:
        #
        # open Chrome
        # open tell me the time
        if not _is_known_application(
            application
        ):
            return None

        commands.append(
            f"open {application}"
        )

    return commands


def _split_mixed_commands(
    command: str,
) -> list[str] | None:

    # Split once:
    #
    # open Chrome and tell me the time
    #
    # becomes:
    #
    # open Chrome
    # tell me the time
    parts = re.split(
        r"\s+and\s+",
        command,
        maxsplit=1,
        flags=re.IGNORECASE,
    )

    if len(parts) != 2:
        return None

    first_command = parts[0].strip()
    second_command = parts[1].strip()

    if (
        not first_command
        or not second_command
    ):
        return None

    # Understand both sides independently.
    first_action = understand_command(
        first_command
    )

    second_action = understand_command(
        second_command
    )

    # Both sides must be valid actions.
    if (
        first_action.name == "unknown"
        or second_action.name == "unknown"
    ):
        return None

    return [
        first_command,
        second_command,
    ]


def create_plan(
    command: str,
    previous_action: Action | None = None,
) -> TaskPlan:

    # ==================================================
    # 1. Multi-open commands
    # ==================================================

    commands = _split_open_commands(
        command
    )

    if commands:

        actions = []

        for single_command in commands:

            action = understand_command(
                single_command
            )

            actions.append(
                action
            )

        return TaskPlan(
            intent="multi_action",
            actions=actions,
        )

    # ==================================================
    # 2. Mixed multi-action commands
    # ==================================================

    commands = _split_mixed_commands(
        command
    )

    if commands:

        actions = []

        for single_command in commands:

            action = understand_command(
                single_command
            )

            action = resolve_context(
                action,
                previous_action,
            )

            actions.append(
                action
            )

        return TaskPlan(
            intent="multi_action",
            actions=actions,
        )

    # ==================================================
    # 3. Single action
    # ==================================================

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