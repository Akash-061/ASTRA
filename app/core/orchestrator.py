from app.core.context import ConversationContext
from app.core.executor import Executor
from app.core.models import (
    AstraResponse,
    UserRequest,
)
from app.core.planner import create_plan
from app.core.response import build_response


class Orchestrator:

    def __init__(
        self,
        context: ConversationContext | None = None,
        executor: Executor | None = None,
    ) -> None:

        self.context = (
            context
            if context is not None
            else ConversationContext()
        )

        self.executor = (
            executor
            if executor is not None
            else Executor()
        )

    def handle(
        self,
        request: UserRequest,
    ) -> AstraResponse:

        self.context.add_message(
            request.text
        )

        # Find the most recent relevant
        # research action rather than blindly
        # using the immediately previous action.
        previous_action = (
            self.context.get_last_action_by_name(
                "research"
            )
        )

        plan = create_plan(
            request.text,
            previous_action=previous_action,
        )

        if plan.intent == "unknown":

            return AstraResponse(
                message=(
                    "I'm not sure how to handle "
                    "that request yet."
                ),
                success=False,
            )

        results = []

        for action in plan.actions:

            # Record every planned action.
            self.context.add_action(
                action
            )

            result = self.executor.execute(
                action
            )

            results.append(result)

        if not results:

            return AstraResponse(
                message="No action was executed.",
                success=False,
            )

        # --------------------------------------------------
        # Build combined multi-action response
        # --------------------------------------------------

        result_messages = [
            result.message
            for result in results
        ]

        all_successful = all(
            result.success
            for result in results
        )

        any_successful = any(
            result.success
            for result in results
        )

        # All actions succeeded.
        if all_successful:

            response = build_response(
                results[-1]
            )

        # Some actions succeeded and some failed.
        elif any_successful:

            response = AstraResponse(
                message=" ".join(
                    result_messages
                ),
                success=False,
                data={},
            )

        # All actions failed.
        else:

            response = build_response(
                results[0]
            )

        # Preserve every execution result.
        response.data["results"] = [
            item.model_dump()
            for item in results
        ]

        return response