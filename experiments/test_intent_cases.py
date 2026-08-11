from app.core.intent import detect_intent


test_cases = [
    ("open Chrome", "open"),
    ("launch calculator", "open"),
    ("start notepad", "open"),
    ("run vscode", "open"),

    ("cpu", "system"),
    ("ram", "system"),
    ("time", "system"),

    ("help", "help"),

    ("exit", "exit"),
    ("quit", "exit"),
    ("bye", "exit"),

    ("search recent news", "research"),
    ("research Chennai", "research"),
    ("look up weather", "research"),
    ("find out what happened", "research"),
    ("what happened in Chennai", "research"),
    ("what's happening in Chennai", "research"),
    ("latest news", "research"),
    ("recent issues", "research"),

    ("play some music", "unknown"),
]


for command, expected in test_cases:

    actual = detect_intent(
        command
    )

    print(
        f"{command!r:35} "
        f"→ {actual:10} "
        f"(expected: {expected})"
    )

    assert actual == expected


print()
print("INTENT CASES PASSED")