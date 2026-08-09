from app.core.context import ConversationContext
from app.core.executor import Executor
from app.core.models import (
    AstraResponse,
    UserRequest,
)
from app.core.planner import create_plan


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

        failed = [
            result
            for result in results
            if not result.success
        ]

        if failed:

            return AstraResponse(
                message=failed[0].message,
                success=False,
            )

        return AstraResponse(
            message=(
                f"Completed task: "
                f"{plan.intent}"
            ),
            success=True,
        )