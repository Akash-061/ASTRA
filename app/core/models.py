from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    text: str


class Action(BaseModel):
    name: str
    parameters: dict = Field(
        default_factory=dict
    )


class ExecutionResult(BaseModel):
    success: bool
    message: str
    data: dict = Field(
        default_factory=dict
    )


class TaskPlan(BaseModel):
    intent: str
    actions: list[Action] = Field(
        default_factory=list
    )


class AstraResponse(BaseModel):
    message: str
    success: bool = True
    data: dict = Field(
        default_factory=dict
    )