from typing import Callable

from app.modules.apps import open_application
from app.modules.help import show_help
from app.modules.research import research
from app.modules.system import handle_system_command


Capability = Callable


CAPABILITIES: dict[str, Capability] = {
    "open": open_application,
    "system": handle_system_command,
    "help": show_help,
    "research": research,
}


def resolve_capability(
    action_name: str,
) -> Capability | None:

    return CAPABILITIES.get(
        action_name
    )