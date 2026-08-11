from app.core.capabilities import FunctionCapability
from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator
from app.core.router import CAPABILITIES


def fake_open(command: str):

    return {
        "success": True,
        "message": "TEST: Chrome opened successfully.",
        "data": {
            "application": "chrome",
        },
    }


original = CAPABILITIES.get("open")


CAPABILITIES["open"] = FunctionCapability(
    fake_open
)


orchestrator = Orchestrator()


request = UserRequest(
    text="open Chrome"
)


response = orchestrator.handle(
    request
)


assert response.success is True

assert (
    response.message
    == "TEST: Chrome opened successfully."
)


CAPABILITIES.pop(
    "open",
    None,
)


if original is not None:

    CAPABILITIES["open"] = original


print("FULL AGENT LOOP PASSED")