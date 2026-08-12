from app.core.assistant import Assistant
from app.core.models import AstraResponse, UserRequest


class FakeOrchestrator:

    def __init__(self):
        self.commands = []

    def handle(self, request):

        self.commands.append(
            request.text
        )

        return AstraResponse(
            message="Assistant handled request.",
            success=True,
            data={
                "command": request.text,
            },
        )


# --------------------------------------------------
# Existing Assistant test
# --------------------------------------------------

fake_orchestrator = FakeOrchestrator()

assistant = Assistant(
    orchestrator=fake_orchestrator
)

response = assistant.handle(
    "test command"
)

assert response.success is True

assert (
    response.message
    == "Assistant handled request."
)

assert (
    response.data["command"]
    == "test command"
)

assert (
    fake_orchestrator.commands
    == ["test command"]
)


# --------------------------------------------------
# Real multi-turn Assistant integration
# --------------------------------------------------

assistant = Assistant()

first_response = assistant.handle(
    "research recent issues in Chennai"
)

assert first_response.success is True


second_response = assistant.handle(
    "what about Bangalore?"
)

assert second_response.success is True


# Access the real orchestrator's context.

context = assistant.orchestrator.context

action = context.get_last_action()

assert action is not None

assert action.name == "research"

assert (
    action.parameters["topic"]
    == "issues"
)

assert (
    action.parameters["location"]
    == "Bangalore"
)

assert (
    action.parameters["timeframe"]
    == "recent"
)


history = context.get_recent()

assert (
    history
    == [
        "research recent issues in Chennai",
        "what about Bangalore?",
    ]
)


print()
print("ASSISTANT PASSED")
print()
print(
    "Multi-turn action:",
    action.parameters,
)