from app.core.understanding import (
    understand_command,
)


tests = [
    (
        "research recent issues in Tokyo",
        "Tokyo",
        "recent",
        "issues",
    ),
    (
        "latest AI developments in Japan",
        "Japan",
        "latest",
        "AI developments",
    ),
    (
        "research Python security",
        None,
        None,
        "Python security",
    ),
]


for (
    command,
    expected_location,
    expected_timeframe,
    expected_topic,
) in tests:

    action = understand_command(
        command
    )

    print()
    print(
        f"Command: {command}"
    )
    print(
        f"Action: {action.name}"
    )
    print(
        f"Parameters: {action.parameters}"
    )

    assert action.name == "research"

    assert (
        action.parameters["topic"]
        == expected_topic
    )

    assert (
        action.parameters.get("location")
        == expected_location
    )

    assert (
        action.parameters.get("timeframe")
        == expected_timeframe
    )


print()
print("RESEARCH UNDERSTANDING PASSED")