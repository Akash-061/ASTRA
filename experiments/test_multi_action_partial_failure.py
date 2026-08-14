from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


orchestrator = Orchestrator()


response = orchestrator.handle(
    UserRequest(
        text="open UnknownApp and tell me the time"
    )
)


print()
print("Response success:", response.success)
print("Response message:", response.message)
print("Response data:", response.data)


# The overall request should report failure
# because one action failed.
assert response.success is False


# But both actions should have been attempted.
results = response.data["results"]

assert len(results) == 2


# First action should fail.
assert results[0]["success"] is False


# Second action should still succeed.
assert results[1]["success"] is True


print()
print("MULTI-ACTION PARTIAL FAILURE PASSED")