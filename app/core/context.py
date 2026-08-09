from dataclasses import dataclass, field


@dataclass
class ConversationContext:
    history: list[str] = field(default_factory=list)

    def add_message(
        self,
        message: str,
    ) -> None:

        self.history.append(message)

    def get_recent(
        self,
        limit: int = 10,
    ) -> list[str]:

        return self.history[-limit:]

    def clear(self) -> None:

        self.history.clear()