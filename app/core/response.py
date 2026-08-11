from app.core.models import AstraResponse, ExecutionResult


def build_response(
    result: ExecutionResult,
) -> AstraResponse:

    if not result.success:

        return AstraResponse(
            message=result.message,
            success=False,
        )

    if result.message:

        return AstraResponse(
            message=result.message,
            success=True,
        )

    return AstraResponse(
        message="Task completed successfully.",
        success=True,
    )