from pydantic import BaseModel


class ResearchRequest(BaseModel):

    topic: str

    location: str | None = None

    timeframe: str | None = None

    scope: str | None = None

    original_query: str = ""