from app.modules.research import research
from app.core.intent import detect_intent
from app.modules.apps import open_application
from app.modules.system import handle_system_command
from app.modules.help import show_help


def route(command: str):

    intent = detect_intent(command)

    if intent == "open":

        open_application(command)

    elif intent == "system":

        handle_system_command(command)
    elif intent == "help":

        show_help()
    elif intent == "exit":

        return False
    elif intent == "research":

        research(command)
    else:

        print(f"Unknown command: {command}")

    return True