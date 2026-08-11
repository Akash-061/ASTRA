from app.core.models import (
    AstraResponse,
    ExecutionResult,
)


def build_response(
    result: ExecutionResult,
) -> AstraResponse:

    if not result.success:

        return AstraResponse(
            message=result.message,
            success=False,
            data=result.data,
        )

    if result.message:

        return AstraResponse(
            message=result.message,
            success=True,
            data=result.data,
        )

    return AstraResponse(
        message="Task completed successfully.",
        success=True,
        data=result.data,
    )