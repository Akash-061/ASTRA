from dataclasses import dataclass, field

from app.core.models import Action


@dataclass
class ConversationContext:

    history: list[str] = field(
        default_factory=list
    )

    last_action: Action | None = None

    action_history: list[Action] = field(
        default_factory=list
    )

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

    def add_action(
        self,
        action: Action,
    ) -> None:

        self.action_history.append(
            action
        )

        self.last_action = action

    def get_action_history(
        self,
    ) -> list[Action]:

        return list(
            self.action_history
        )

    def clear(self) -> None:

        self.history.clear()

        self.last_action = None

        self.action_history.clear()