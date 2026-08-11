from app.core.understanding import (
    understand_command,
)


tests = [
    (
        "cpu",
        "system",
        "cpu",
    ),
    (
        "How much CPU am I using?",
        "system",
        "cpu",
    ),
    (
        "ram",
        "system",
        "ram",
    ),
    (
        "How much RAM am I using?",
        "system",
        "ram",
    ),
    (
        "How much memory is being used?",
        "system",
        "ram",
    ),
    (
        "What time is it?",
        "system",
        "time",
    ),
    (
        "open Chrome",
        "open",
        "Chrome",
    ),
    (
        "launch calculator",
        "open",
        "calculator",
    ),
    (
        "help",
        "help",
        None,
    ),
]


for command, expected_name, expected_value in tests:

    action = understand_command(
        command
    )

    print(
        f"{command!r} "
        f"→ {action.name} "
        f"{action.parameters}"
    )

    assert (
        action.name
        == expected_name
    )

    if expected_value is not None:

        if expected_name == "system":

            assert (
                action.parameters["command"]
                == expected_value
            )

        elif expected_name == "open":

            assert (
                action.parameters["application"]
                == expected_value
            )


print()
print("UNDERSTANDING PASSED")