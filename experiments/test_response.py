from app.core.models import ExecutionResult
from app.core.response import build_response


# --------------------------------------------------
# Successful response with data
# --------------------------------------------------

result = ExecutionResult(
    success=True,
    message="Chrome opened successfully.",
    data={
        "application": "Chrome",
        "action": "open",
    },
)


response = build_response(
    result
)


assert response.success is True

assert (
    response.message
    == "Chrome opened successfully."
)

assert (
    response.data["application"]
    == "Chrome"
)

assert (
    response.data["action"]
    == "open"
)


# --------------------------------------------------
# Failed response with data
# --------------------------------------------------

failed_result = ExecutionResult(
    success=False,
    message="Chrome could not be opened.",
    data={
        "application": "Chrome",
        "reason": "not found",
    },
)


failed_response = build_response(
    failed_result
)


assert failed_response.success is False

assert (
    failed_response.message
    == "Chrome could not be opened."
)

assert (
    failed_response.data["application"]
    == "Chrome"
)

assert (
    failed_response.data["reason"]
    == "not found"
)


print("RESPONSE BUILDER PASSED")