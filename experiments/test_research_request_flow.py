from app.core.models import Action

from app.research.adapter import (
    action_to_research_request,
)


test_cases = [
    (
        "research recent issues in Tokyo",
        {
            "topic": "issues",
            "location": "Tokyo",
            "timeframe": "recent",
        },
    ),

    (
        "research current traffic problems in Chennai",
        {
            "topic": "traffic problems",
            "location": "Chennai",
            "timeframe": "current",
        },
    ),

    (
        "research latest news in London",
        {
            "topic": "news",
            "location": "London",
            "timeframe": "latest",
        },
    ),
]


print()
print("================================")
print("RESEARCH REQUEST FLOW TEST")
print("================================")


for command, expected in test_cases:

    action = Action(
        name="research",
        parameters={
            "command": command,
            "topic": expected["topic"],
            "location": expected["location"],
            "timeframe": expected["timeframe"],
        },
    )

    request = action_to_research_request(
        action
    )

    print()
    print(
        f"Command: {command}"
    )

    print(
        f"Topic: {request.topic}"
    )

    print(
        f"Location: {request.location}"
    )

    print(
        f"Timeframe: {request.timeframe}"
    )

    print(
        f"Original query: "
        f"{request.original_query}"
    )

    assert (
        request.topic
        == expected["topic"]
    )

    assert (
        request.location
        == expected["location"]
    )

    assert (
        request.timeframe
        == expected["timeframe"]
    )

    assert (
        request.original_query
        == command
    )


print()
print(
    "RESEARCH REQUEST FLOW PASSED"
)