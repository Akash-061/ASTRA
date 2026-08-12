from app.core.intent import detect_intent
from app.core.models import Action

from app.research.parameters import (
    extract_location,
    extract_research_topic,
    extract_timeframe,
)


def understand_command(
    command: str,
) -> Action:

    intent = detect_intent(
        command
    )

    # --------------------------------------------------
    # System commands
    # --------------------------------------------------

    if intent == "system":

        lowered = command.lower()

        if (
            "cpu" in lowered
            or "processor" in lowered
        ):

            return Action(
                name="system",
                parameters={
                    "command": "cpu",
                },
            )

        if (
            "ram" in lowered
            or "memory" in lowered
        ):

            return Action(
                name="system",
                parameters={
                    "command": "ram",
                },
            )

        if (
            "time" in lowered
            or "what time" in lowered
        ):

            return Action(
                name="system",
                parameters={
                    "command": "time",
                },
            )

    # --------------------------------------------------
    # Open commands
    # --------------------------------------------------

    if intent == "open":

        command_lower = command.lower()

        for word in [
            "open",
            "launch",
            "start",
            "run",
        ]:

            if command_lower.startswith(
                word + " "
            ):

                application = command[
                    len(word):
                ].strip()

                return Action(
                    name="open",
                    parameters={
                        "command": command,
                        "application": application,
                    },
                )

    # --------------------------------------------------
    # Research commands
    # --------------------------------------------------

    if intent == "research":

        topic = extract_research_topic(
            command
        )

        location = extract_location(
            command
        )

        timeframe = extract_timeframe(
            command
        )

        parameters = {
            "command": command,
            "topic": topic,
        }

        if location:

            parameters["location"] = (
                location
            )

        if timeframe:

            parameters["timeframe"] = (
                timeframe
            )

        return Action(
            name="research",
            parameters=parameters,
        )

    # --------------------------------------------------
    # Help
    # --------------------------------------------------

    if intent == "help":

        return Action(
            name="help",
            parameters={},
        )

    # --------------------------------------------------
    # Exit
    # --------------------------------------------------

    if intent == "exit":

        return Action(
            name="exit",
            parameters={},
        )

    # --------------------------------------------------
    # Unknown
    # --------------------------------------------------

    return Action(
        name="unknown",
        parameters={
            "command": command,
        },
    )