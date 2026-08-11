from app.research.models import Claim
from app.research.request import ResearchRequest

from app.research.relevance import (
    calculate_contextual_relevance,
    is_contextually_relevant,
)


request = ResearchRequest(
    topic="issues",
    location="Chennai",
    timeframe="recent",
    original_query="recent issues in Chennai",
)


test_cases = [

    (
        "KEEP",
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
    ),

    (
        "KEEP",
        Claim(
            statement=(
                "Parking shortages and traffic "
                "congestion are affecting "
                "Anna Nagar residents."
            ),
            source_title=(
                "Anna Nagar faces civic strain"
            ),
            source_url=(
                "https://example.com/"
                "cities/chennai/anna-nagar"
            ),
        ),
    ),

    (
        "KEEP",
        Claim(
            statement=(
                "Street name boards were damaged "
                "in Kodungaiyur and residents "
                "requested repairs."
            ),
            source_title=(
                "Kodungaiyur civic issues need attention"
            ),
            source_url=(
                "https://example.com/"
                "cities/chennai/kodungaiyur"
            ),
        ),
    ),

    (
        "REJECT",
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
    ),

    (
        "REJECT",
        Claim(
            statement=(
                "A major traffic disruption "
                "was reported in London."
            ),
            source_title=(
                "London traffic disruption"
            ),
            source_url=(
                "https://example.com/"
                "london/traffic"
            ),
        ),
    ),

    (
        "REJECT",
        Claim(
            statement=(
                "A new movie starring a popular "
                "actor was released in Chennai."
            ),
            source_title=(
                "New movie released in Chennai"
            ),
            source_url=(
                "https://example.com/"
                "movies/chennai"
            ),
        ),
    ),

    (
        "REJECT",
        Claim(
            statement=(
                "Global economic uncertainty "
                "continues to affect markets "
                "around the world."
            ),
            source_title=(
                "Global economic uncertainty"
            ),
            source_url=(
                "https://example.com/"
                "world/economy"
            ),
        ),
    ),
]


print()
print("================================================")
print("RELEVANCE DECISION MATRIX")
print("================================================")


passed = 0
failed = 0


for index, (
    expected,
    claim,
) in enumerate(
    test_cases,
    start=1,
):

    scores = calculate_contextual_relevance(
        request,
        claim,
    )

    relevant = is_contextually_relevant(
        request,
        claim,
    )

    actual = (
        "KEEP"
        if relevant
        else "REJECT"
    )

    status = (
        "PASS"
        if actual == expected
        else "FAIL"
    )

    if status == "PASS":
        passed += 1
    else:
        failed += 1

    print()
    print(
        f"Claim {index}: "
        f"{status}"
    )

    print(
        f"Expected : {expected}"
    )

    print(
        f"Actual   : {actual}"
    )

    print(
        f"Statement: "
        f"{claim.statement}"
    )

    print(
        f"Semantic : "
        f"{scores['semantic']:.3f}"
    )

    print(
        f"Title    : "
        f"{scores['title']:.3f}"
    )

    print(
        f"URL      : "
        f"{scores['url']:.3f}"
    )

    print(
        f"Location : "
        f"{scores['location']:.3f}"
    )

    print(
        f"Issue    : "
        f"{scores['issue']:.3f}"
    )

    print(
        f"Final    : "
        f"{scores['final']:.3f}"
    )


print()
print("================================================")
print("RESULT")
print("================================================")

print(
    f"Passed: {passed}/{len(test_cases)}"
)

print(
    f"Failed: {failed}/{len(test_cases)}"
)

if failed > 0:

    raise AssertionError(
        "RELEVANCE MATRIX FAILED"
    )

print()
print("RELEVANCE MATRIX PASSED")