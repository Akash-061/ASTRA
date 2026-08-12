from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


request = UserRequest(
    text="open Chrome"
)


response = orchestrator.handle(
    request
)


assert response.success is True


action_history = (
    orchestrator.context.get_action_history()
)


assert len(action_history) == 1

assert (
    action_history[0].name
    == "open"
)

assert (
    action_history[0].parameters["application"]
    == "Chrome"
)


assert (
    orchestrator.context.get_last_action()
    == action_history[0]
)


print()
print("ORCHESTRATOR ACTION HISTORY PASSED")