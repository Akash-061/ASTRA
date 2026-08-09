from app.research.models import Claim
from app.research.semantic_relevance import (
    calculate_semantic_relevance,
)
from app.research.relevance import (
    calculate_text_similarity,
)


query = "recent issues in Chennai"


claims = [

    Claim(
        statement=(
            "Residents in Adyar reported "
            "frequent power interruptions."
        ),
        source_title=(
            "Chennai power outages affect residents"
        ),
        source_url=(
            "https://example.com/cities/chennai/power"
        ),
    ),

    Claim(
        statement=(
            "Chennai is one of many cities "
            "affected by global water shortages."
        ),
        source_title="Global water crisis",
        source_url=(
            "https://example.com/world/water-crisis"
        ),
    ),

    Claim(
        statement=(
            "A school shooting occurred in Thailand."
        ),
        source_title="Thailand school shooting",
        source_url=(
            "https://example.com/thailand/news"
        ),
    ),
]


for claim in claims:

    semantic_score = calculate_semantic_relevance(
        query,
        claim,
    )

    title_score = calculate_text_similarity(
        query,
        claim.source_title,
    )

    url_score = calculate_text_similarity(
        query,
        claim.source_url,
    )

    hybrid_score = (
        semantic_score * 0.60
        + title_score * 0.25
        + url_score * 0.15
    )

    print("\nClaim:")
    print(claim.statement)

    print(f"Semantic: {semantic_score:.3f}")
    print(f"Title:    {title_score:.3f}")
    print(f"URL:      {url_score:.3f}")
    print(f"HYBRID:   {hybrid_score:.3f}")