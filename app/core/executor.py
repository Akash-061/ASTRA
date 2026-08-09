from app.core.models import Action, ExecutionResult
from app.core.router import resolve_capability


class Executor:

    def execute(
        self,
        action: Action,
    ) -> ExecutionResult:

        capability = resolve_capability(
            action.name
        )

        if capability is None:

            return ExecutionResult(
                success=False,
                message=(
                    f"No capability found for "
                    f"action: {action.name}"
                ),
            )

        command = action.parameters.get(
            "command",
            "",
        )

        try:

            result = capability(
                command
            )

            return ExecutionResult(
                success=True,
                message=(
                    f"Action '{action.name}' "
                    f"executed successfully."
                ),
                data={
                    "result": result,
                },
            )

        except Exception as error:

            return ExecutionResult(
                success=False,
                message=(
                    f"Action '{action.name}' "
                    f"failed: {error}"
                ),
            )