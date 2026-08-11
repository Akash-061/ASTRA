from abc import ABC, abstractmethod

from app.core.models import Action, ExecutionResult


class Capability(ABC):

    @abstractmethod
    def execute(
        self,
        action: Action,
    ) -> ExecutionResult:
        pass