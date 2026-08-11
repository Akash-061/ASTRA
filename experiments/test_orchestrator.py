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

        plan = create_plan(
            request.text
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

            result = self.executor.execute(
                action
            )

            results.append(result)

        if not results:

            return AstraResponse(
                message="No action was executed.",
                success=False,
            )

        # If any action fails, return the
        # failed result while preserving
        # all execution results.
        for result in results:

            if not result.success:

                response = build_response(
                    result
                )

                response.data["results"] = [
                    item.model_dump()
                    for item in results
                ]

                return response

        # Use the last successful result
        # as the primary user-facing response.
        response = build_response(
            results[-1]
        )

        # Preserve every execution result
        # for callers that need structured data.
        response.data["results"] = [
            item.model_dump()
            for item in results
        ]

        return response