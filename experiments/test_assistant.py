from app.core.assistant import Assistant
from app.core.models import AstraResponse


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


print("ASSISTANT PASSED")