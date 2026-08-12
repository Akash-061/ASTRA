from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


request = UserRequest(
    text="this is definitely an unknown command"
)


response = orchestrator.handle(
    request
)


assert response.success is False


assert (
    orchestrator.context.get_action_history()
    == []
)


assert (
    orchestrator.context.get_last_action()
    is None
)


print()
print("FAILED ACTION MEMORY PASSED")