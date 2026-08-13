from app.core.models import Action

from app.research.parameters import (
    extract_location,
    extract_timeframe,
)


AMBIGUOUS_REFERENCES = {
    "it",
    "that",
    "this",
    "the same",
    "the other one",
    "the other",
}


KNOWN_LOCATIONS = {
    "bangalore",
    "bengaluru",
    "chennai",
    "mumbai",
    "delhi",
    "new delhi",
    "kolkata",
    "hyderabad",
    "pune",
    "coimbatore",
    "madurai",
    "india",
    "japan",
    "china",
    "usa",
    "united states",
    "uk",
    "united kingdom",
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


def _is_ambiguous_followup(
    command: str,
) -> bool:

    value = _extract_followup_value(
        command
    )

    if value is None:
        return False

    normalized = value.lower().strip()

    return (
        normalized in AMBIGUOUS_REFERENCES
    )


def _is_known_location(
    value: str,
) -> bool:

    normalized = value.lower().strip()

    return normalized in KNOWN_LOCATIONS


def resolve_context(
    new_action: Action,
    previous_action: Action | None = None,
) -> Action:

    # --------------------------------------------------
    # No previous context
    # --------------------------------------------------

    if previous_action is None:
        return new_action

    # --------------------------------------------------
    # Context currently applies only to
    # research follow-up commands
    # --------------------------------------------------

    if previous_action.name != "research":
        return new_action

    if new_action.name != "unknown":
        return new_action

    command = new_action.parameters.get(
        "command",
        "",
    )

    # --------------------------------------------------
    # Safety: reject ambiguous references
    # --------------------------------------------------

    if _is_ambiguous_followup(
        command
    ):
        return new_action

    previous_parameters = (
        previous_action.parameters
    )

    # --------------------------------------------------
    # Extract explicit parameters
    # --------------------------------------------------

    timeframe = extract_timeframe(
        command
    )

    location = extract_location(
        command
    )

    followup_value = (
        _extract_followup_value(
            command
        )
    )

    followup_topic = None

    # --------------------------------------------------
    # Handle "what about X?"
    #
    # If X is a known location, replace
    # the previous location.
    #
    # Otherwise, treat X as a new topic.
    # --------------------------------------------------

    if followup_value:

        if _is_known_location(
            followup_value
        ):

            location = followup_value

        else:

            followup_topic = (
                followup_value
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
    # Nothing new was provided
    # --------------------------------------------------

    if (
        followup_topic is None
        and location is None
        and timeframe is None
    ):
        return new_action

    # --------------------------------------------------
    # Build resolved action
    # --------------------------------------------------

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