from pydantic import BaseModel


class SearchResult(BaseModel):

    title: str
    url: str
    snippet: str = ""
    source: str = ""
    published_date: str | None = None


class Claim(BaseModel):

    statement: str
    sources: list[str] = []
    confidence: float = 0.0