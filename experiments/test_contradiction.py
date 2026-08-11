from app.research.models import Claim

from app.research.contradiction import (
    calculate_contradiction_score,
    are_contradictory,
)


test_cases = [

    (
        "CONTRADICTION",
        Claim(
            statement=(
                "Chennai airport operations "
                "resumed normally."
            )
        ),
        Claim(
            statement=(
                "Chennai airport operations "
                "remain disrupted."
            )
        ),
        True,
    ),

    (
        "CONTRADICTION",
        Claim(
            statement=(
                "The road is open to traffic."
            )
        ),
        Claim(
            statement=(
                "The road is closed to traffic."
            )
        ),
        True,
    ),

    (
        "AGREEMENT",
        Claim(
            statement=(
                "Power outages affected "
                "residents in Adyar."
            )
        ),
        Claim(
            statement=(
                "Adyar residents experienced "
                "power interruptions."
            )
        ),
        False,
    ),

    (
        "UNRELATED",
        Claim(
            statement=(
                "A school shooting occurred "
                "in Thailand."
            )
        ),
        Claim(
            statement=(
                "The Chennai metro added "
                "a new route."
            )
        ),
        False,
    ),
]


print()
print("================================")
print("CONTRADICTION VALIDATION")
print("================================")


for index, (
    expected,
    claim_a,
    claim_b,
    expected_result,
) in enumerate(
    test_cases,
    start=1,
):

    score = calculate_contradiction_score(
        claim_a,
        claim_b,
    )

    actual_result = are_contradictory(
        claim_a,
        claim_b,
    )

    print()
    print(
        f"Test {index}: {expected}"
    )

    print(
        f"Score: {score:.3f}"
    )

    print(
        f"Expected: "
        f"{expected_result}"
    )

    print(
        f"Actual:   "
        f"{actual_result}"
    )

    assert (
        actual_result
        == expected_result
    )


print()
print(
    "CONTRADICTION VALIDATION PASSED"
)