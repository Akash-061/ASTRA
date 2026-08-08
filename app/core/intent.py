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


def detect_intent(command: str):

    command = command.lower().strip()

    for word in OPEN_COMMANDS:

        if command.startswith(word + " "):
            return "open"

    if command in SYSTEM_COMMANDS:
        return "system"

    if command in HELP_COMMANDS:
        return "help"

    if command in EXIT_COMMANDS:
        return "exit"

    # Check for research requests
    for phrase in RESEARCH_COMMANDS:

        if phrase in command:
            return "research"

    return "unknown"