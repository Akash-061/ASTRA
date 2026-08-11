OPEN_COMMANDS = [
    "open",
    "launch",
    "start",
    "run",
]

SYSTEM_COMMANDS = [
    "cpu",
    "ram",
    "time",
]

HELP_COMMANDS = [
    "help",
]

EXIT_COMMANDS = [
    "exit",
    "quit",
    "bye",
]

RESEARCH_COMMANDS = [
    "search",
    "research",
    "look up",
    "find out",
    "what happened",
    "what's happening",
    "latest",
    "recent",
]


SYSTEM_PHRASES = [
    "cpu usage",
    "processor usage",
    "processor load",
    "how much cpu",
    "cpu being used",
    "cpu am i using",

    "ram usage",
    "memory usage",
    "how much ram",
    "how much memory",
    "ram being used",
    "memory being used",
    "ram am i using",

    "current time",
    "what time is it",
    "tell me the time",
    "what's the time",
]


def detect_intent(
    command: str,
) -> str:

    command = command.lower().strip()

    if not command:
        return "unknown"

    for word in OPEN_COMMANDS:

        if command.startswith(
            word + " "
        ):

            return "open"

    if command in SYSTEM_COMMANDS:

        return "system"

    if command in HELP_COMMANDS:

        return "help"

    if command in EXIT_COMMANDS:

        return "exit"

    for phrase in SYSTEM_PHRASES:

        if phrase in command:

            return "system"

    for phrase in RESEARCH_COMMANDS:

        if phrase in command:

            return "research"

    return "unknown"