from app.core.models import ExecutionResult
from app.core.response import build_response


result = ExecutionResult(
    success=True,
    message="Chrome opened successfully.",
)


response = build_response(
    result
)


assert response.success is True

assert (
    response.message
    == "Chrome opened successfully."
)


failed_result = ExecutionResult(
    success=False,
    message="Chrome could not be opened.",
)


failed_response = build_response(
    failed_result
)


assert failed_response.success is False

assert (
    failed_response.message
    == "Chrome could not be opened."
)


print("RESPONSE BUILDER PASSED")