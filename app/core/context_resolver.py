from app.core.models import Action

from app.research.parameters import (
    extract_location,
    extract_timeframe,
)


KNOWN_LOCATIONS = {
    "india",
    "japan",
    "tokyo",
    "chennai",
    "bangalore",
    "bengaluru",
    "delhi",
    "mumbai",
    "hyderabad",
    "kolkata",
    "kerala",
    "tamil nadu",
    "usa",
    "united states",
    "uk",
    "united kingdom",
    "china",
    "singapore",
    "australia",
    "canada",
    "germany",
    "france",
}


def _extract_followup_value(
    command: str,
) -> str | None:

    lowered = command.lower().strip()

    prefixes = [
        "what about ",
        "how about ",
    ]

    for prefix in prefixes:

        if lowered.startswith(prefix):

            value = command[
                len(prefix):
            ].strip()

            value = value.rstrip(
                "?.!"
            ).strip()

            if value:
                return value

    return None


def _is_known_location(
    value: str | None,
) -> bool:

    if not value:
        return False

    return (
        value.lower().strip()
        in KNOWN_LOCATIONS
    )


def resolve_context(
    new_action: Action,
    previous_action: Action | None = None,
) -> Action:

    if previous_action is None:
        return new_action

    if previous_action.name != "research":
        return new_action

    if new_action.name != "unknown":
        return new_action

    previous_parameters = (
        previous_action.parameters
    )

    command = new_action.parameters.get(
        "command",
        "",
    )

    # --------------------------------------------------
    # Extract explicit timeframe
    # --------------------------------------------------

    timeframe = extract_timeframe(
        command
    )

    # --------------------------------------------------
    # Extract "what about X?"
    # --------------------------------------------------

    followup_value = (
        _extract_followup_value(
            command
        )
    )

    location = None
    followup_topic = None

    if followup_value:

        if _is_known_location(
            followup_value
        ):

            location = followup_value

        else:

            followup_topic = followup_value

    else:

        # Handle explicit location phrases such as:
        #
        # "in Bangalore"
        # "from Japan"
        # "at Tokyo"

        location = extract_location(
            command
        )

    # --------------------------------------------------
    # Previous parameters
    # --------------------------------------------------

    previous_topic = (
        previous_parameters.get(
            "topic"
        )
    )

    previous_location = (
        previous_parameters.get(
            "location"
        )
    )

    previous_timeframe = (
        previous_parameters.get(
            "timeframe"
        )
    )

    # --------------------------------------------------
    # Apply overrides
    # --------------------------------------------------

    resolved_topic = (
        followup_topic
        if followup_topic
        else previous_topic
    )

    resolved_location = (
        location
        if location
        else previous_location
    )

    resolved_timeframe = (
        timeframe
        if timeframe
        else previous_timeframe
    )

    # --------------------------------------------------
    # Nothing to resolve
    # --------------------------------------------------

    if (
        followup_topic is None
        and location is None
        and timeframe is None
    ):
        return new_action

    parameters = {
        "command": command,
        "topic": resolved_topic or "",
    }

    if resolved_location:

        parameters["location"] = (
            resolved_location
        )

    if resolved_timeframe:

        parameters["timeframe"] = (
            resolved_timeframe
        )

    return Action(
        name="research",
        parameters=parameters,
    )