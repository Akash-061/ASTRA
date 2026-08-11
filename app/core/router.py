from app.core.capabilities import FunctionCapability
from app.modules.apps import open_application
from app.modules.help import show_help
from app.modules.research import research
from app.modules.system import handle_system_command


CAPABILITIES = {
    "open": FunctionCapability(
        open_application
    ),
    "system": FunctionCapability(
        handle_system_command
    ),
    "help": FunctionCapability(
        show_help
    ),
    "research": FunctionCapability(
        research
    ),
}


def resolve_capability(
    action_name: str,
):

    return CAPABILITIES.get(
        action_name
    )