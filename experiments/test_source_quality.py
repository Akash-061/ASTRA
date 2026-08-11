from app.research.source_quality import (
    calculate_source_quality,
    classify_source,
)


test_cases = [

    (
        "https://www.reuters.com/world/asia",
        "high",
    ),

    (
        "https://www.bbc.com/news/world",
        "high",
    ),

    (
        "https://example.gov.in/news",
        "high",
    ),

    (
        "https://university.edu/research",
        "high",
    ),

    (
        "https://unknown-example.com/article",
        "unknown",
    ),
]


print()
print("================================")
print("SOURCE QUALITY TEST")
print("================================")


for url, expected_class in test_cases:

    score = calculate_source_quality(
        url
    )

    actual_class = classify_source(
        url
    )

    print()
    print(
        f"URL: {url}"
    )

    print(
        f"Score: {score:.3f}"
    )

    print(
        f"Classification: "
        f"{actual_class}"
    )

    assert (
        actual_class
        == expected_class
    )


print()
print("SOURCE QUALITY PASSED")