import re


TIMEFRAME_WORDS = [
    "today",
    "tonight",
    "yesterday",
    "recent",
    "recently",
    "latest",
    "current",
    "currently",
    "now",
    "this week",
    "this month",
    "this year",
]


def extract_timeframe(
    text: str,
) -> str | None:

    lowered = text.lower()

    for timeframe in sorted(
        TIMEFRAME_WORDS,
        key=len,
        reverse=True,
    ):

        if timeframe in lowered:
            return timeframe

    return None


def extract_location(
    text: str,
) -> str | None:

    patterns = [
        r"\bin\s+([A-Za-z][A-Za-z .'-]*)",
        r"\bat\s+([A-Za-z][A-Za-z .'-]*)",
        r"\bfrom\s+([A-Za-z][A-Za-z .'-]*)",
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:

            location = match.group(
                1
            ).strip()

            location = re.split(
                r"\b(?:today|tonight|yesterday|recent|recently|latest|current|currently|now)\b",
                location,
                flags=re.IGNORECASE,
            )[0].strip()

            if location:
                return location

    return None


def extract_research_topic(
    text: str,
) -> str:

    topic = text.strip()

    prefixes = [
        "search the web for ",
        "search the web ",
        "search for ",
        "search ",
        "research ",
        "look up ",
        "find out ",
    ]

    lowered = topic.lower()

    for prefix in prefixes:

        if lowered.startswith(prefix):

            topic = topic[
                len(prefix):
            ].strip()

            break

    # Remove timeframe phrases from the topic.
    for timeframe in sorted(
        TIMEFRAME_WORDS,
        key=len,
        reverse=True,
    ):

        topic = re.sub(
            rf"\b{re.escape(timeframe)}\b",
            "",
            topic,
            flags=re.IGNORECASE,
        )

    # Remove common location phrases.
    topic = re.sub(
        r"\b(?:in|at|from)\s+"
        r"[A-Za-z][A-Za-z .'-]*$",
        "",
        topic,
        flags=re.IGNORECASE,
    )

    topic = re.sub(
        r"\s+",
        " ",
        topic,
    ).strip()

    return topic