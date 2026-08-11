from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


request = UserRequest(
    text="cpu"
)


response = orchestrator.handle(
    request
)


assert response.success is True

assert "CPU Usage:" in response.message


print()
print("ASTRA RESPONSE:")
print(response.message)
print()
print("SYSTEM AGENT PASSED")