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

        return capability.execute(
            action
        )