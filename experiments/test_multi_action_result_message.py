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


# Overall request still fails because
# one of the actions failed.
assert response.success is False


# But the final message should represent
# both the failure and the successful action.
assert "Unknown application" in response.message

assert (
    "Current Time"
    in response.message
)


results = response.data["results"]

assert len(results) == 2

assert results[0]["success"] is False

assert results[1]["success"] is True


print()
print("MULTI-ACTION RESULT MESSAGE PASSED")
