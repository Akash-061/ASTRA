from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


request = UserRequest(
    text="unknown command"
)


response = orchestrator.handle(
    request
)


assert response.success is False

assert (
    response.message
    == "I'm not sure how to handle "
       "that request yet."
)


assert (
    orchestrator.context.get_recent()
    == ["unknown command"]
)


print("ORCHESTRATOR PASSED")