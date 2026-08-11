from app.core.models import AstraResponse, UserRequest
from app.core.orchestrator import Orchestrator


class Assistant:

    def __init__(
        self,
        orchestrator: Orchestrator | None = None,
    ) -> None:

        self.orchestrator = (
            orchestrator
            if orchestrator is not None
            else Orchestrator()
        )

    def handle(
        self,
        text: str,
    ) -> AstraResponse:

        request = UserRequest(
            text=text
        )

        return self.orchestrator.handle(
            request
        )