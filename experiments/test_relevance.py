from app.research.models import Claim
from app.research.relevance import (
    calculate_relevance,
    is_relevant,
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

    score = calculate_relevance(
        query,
        claim,
    )

    relevant = is_relevant(
        query,
        claim,
    )

    print(
        f"{score:.3f} | "
        f"{relevant} | "
        f"{claim.statement}"
    )