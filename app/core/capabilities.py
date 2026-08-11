from app.core.capability import Capability
from app.core.models import Action, ExecutionResult


class FunctionCapability(Capability):

    def __init__(
        self,
        function,
    ) -> None:

        self.function = function

    def execute(
        self,
        action: Action,
    ) -> ExecutionResult:

        try:

            # Functions that explicitly want the
            # complete Action can declare this
            # attribute.
            if getattr(
                self.function,
                "accepts_action",
                False,
            ):

                result = self.function(
                    action
                )

            else:

                parameters = action.parameters

                if parameters:

                    if "command" in parameters:

                        result = self.function(
                            parameters["command"]
                        )

                    else:

                        result = self.function(
                            **parameters
                        )

                else:

                    result = self.function()

            # If the capability already returned
            # an ExecutionResult, preserve it exactly.
            if isinstance(
                result,
                ExecutionResult,
            ):

                return result

            # Convert dictionary results into the
            # standard ExecutionResult contract.
            if isinstance(
                result,
                dict,
            ):

                success = result.get(
                    "success",
                    True,
                )

                message = result.get(
                    "message",
                    "Task completed successfully.",
                )

                data = result.get(
                    "data",
                    {},
                )

                extra_data = {
                    key: value
                    for key, value in result.items()
                    if key not in {
                        "success",
                        "message",
                        "data",
                    }
                }

                data = {
                    **data,
                    **extra_data,
                }

                return ExecutionResult(
                    success=success,
                    message=message,
                    data=data,
                )

            # Handle simple string/other return values.
            return ExecutionResult(
                success=True,
                message=str(result),
                data={},
            )

        except Exception as error:

            return ExecutionResult(
                success=False,
                message=(
                    f"Action '{action.name}' "
                    f"failed: {error}"
                ),
            )