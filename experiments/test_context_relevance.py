from app.research.models import Claim
from app.research.request import ResearchRequest

from app.research.relevance import (
    calculate_contextual_relevance,
)


request = ResearchRequest(
    topic="issues",
    location="Chennai",
    timeframe="recent",
    original_query=(
        "recent issues in Chennai"
    ),
)


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
            "https://example.com/"
            "cities/chennai/power"
        ),
    ),

    Claim(
        statement=(
            "Chennai is one of many cities "
            "affected by global water shortages."
        ),
        source_title=(
            "Global water crisis"
        ),
        source_url=(
            "https://example.com/"
            "world/water-crisis"
        ),
    ),

    Claim(
        statement=(
            "A school shooting occurred "
            "in Thailand."
        ),
        source_title=(
            "Thailand school shooting"
        ),
        source_url=(
            "https://example.com/"
            "thailand/news"
        ),
    ),
]


for index, claim in enumerate(
    claims,
    start=1,
):

    scores = (
        calculate_contextual_relevance(
            request,
            claim,
        )
    )

    print()
    print(
        f"Claim {index}: "
        f"{claim.statement}"
    )

    print(
        f"Semantic:  "
        f"{scores['semantic']:.3f}"
    )

    print(
        f"Title:     "
        f"{scores['title']:.3f}"
    )

    print(
        f"URL:       "
        f"{scores['url']:.3f}"
    )

    print(
        f"Location:  "
        f"{scores['location']:.3f}"
    )

    print(
        f"Issue:     "
        f"{scores['issue']:.3f}"
    )

    print(
        f"FINAL:     "
        f"{scores['final']:.3f}"
    )


print()
print(
    "CONTEXT RELEVANCE PASSED"
)