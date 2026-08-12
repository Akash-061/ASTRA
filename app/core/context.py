from dataclasses import dataclass, field

from app.core.models import Action


@dataclass
class ConversationContext:

    history: list[str] = field(
        default_factory=list
    )

    last_action: Action | None = None

    def add_message(
        self,
        message: str,
    ) -> None:

        self.history.append(
            message
        )

    def get_recent(
        self,
        limit: int = 10,
    ) -> list[str]:

        return self.history[-limit:]

    def set_last_action(
        self,
        action: Action,
    ) -> None:

        self.last_action = action

    def get_last_action(
        self,
    ) -> Action | None:

        return self.last_action

    def clear(self) -> None:

        self.history.clear()

        self.last_action = None