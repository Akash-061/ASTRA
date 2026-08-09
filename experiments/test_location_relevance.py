from app.research.models import Claim

from app.research.location_relevance import (
    calculate_location_relevance,
    is_location_relevant,
)


claims = [

    Claim(
        statement=(
            "Recurring power outages have affected "
            "residents in Adyar."
        ),
        source_title=(
            "Chennai power outages continue to affect residents"
        ),
        source_url=(
            "https://example.com/cities/chennai/power"
        ),
    ),

    Claim(
        statement=(
            "Street name boards were damaged in Kodungaiyur "
            "and residents requested repairs."
        ),
        source_title=(
            "Kodungaiyur civic issues need attention"
        ),
        source_url=(
            "https://example.com/cities/chennai/kodungaiyur"
        ),
    ),

    Claim(
        statement=(
            "Parking shortages and traffic congestion "
            "are affecting Anna Nagar residents."
        ),
        source_title=(
            "Anna Nagar faces civic strain"
        ),
        source_url=(
            "https://example.com/cities/chennai/anna-nagar"
        ),
    ),

    Claim(
        statement=(
            "A school shooting occurred in Thailand."
        ),
        source_title=(
            "Thailand school shooting"
        ),
        source_url=(
            "https://example.com/thailand/news"
        ),
    ),

    Claim(
        statement=(
            "A global economic crisis is affecting "
            "markets around the world."
        ),
        source_title=(
            "Global economic crisis"
        ),
        source_url=(
            "https://example.com/world/economy"
        ),
    ),
]


locations = [
    "Chennai",
    "Adyar",
    "OMR",
    "Kodungaiyur",
    "Anna Nagar",
    "Thailand",
]


for location in locations:

    print()
    print("================================")
    print(f"LOCATION: {location}")
    print("================================")

    for index, claim in enumerate(
        claims,
        start=1,
    ):

        score = calculate_location_relevance(
            location,
            claim,
        )

        relevant = is_location_relevant(
            location,
            claim,
        )

        print(
            f"Claim {index} | "
            f"Score: {score:.3f} | "
            f"Relevant: {relevant}"
        )