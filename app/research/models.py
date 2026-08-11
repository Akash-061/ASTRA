from pydantic import BaseModel, Field


class SearchResult(BaseModel):

    title: str
    url: str
    snippet: str = ""
    source: str = ""
    published_date: str | None = None


class Claim(BaseModel):

    statement: str
    sources: list[str] = Field(
        default_factory=list
    )

    source_title: str = ""
    source_url: str = ""

    confidence: float = 0.0


class EvidenceGroup(BaseModel):

    representative_claim: str

    claims: list[Claim] = Field(
        default_factory=list
    )

    sources: list[str] = Field(
        default_factory=list
    )

    domains: list[str] = Field(
        default_factory=list
    )

    confidence: float = 0.0

    has_conflict: bool = False

    conflicting_claims: list[Claim] = Field(
        default_factory=list
    )