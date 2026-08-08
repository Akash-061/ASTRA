from app.research.conflicts import detect_conflicts


claims = [

    (
        "Chennai project",
        "The project will start Monday.",
        "https://source-a.com/article",
    ),

    (
        "Chennai project",
        "The project will start Wednesday.",
        "https://source-b.com/article",
    ),

    (
        "Chennai weather",
        "Heavy rain is expected.",
        "https://source-c.com/article",
    ),
]


conflicts = detect_conflicts(claims)


print(f"Conflicts found: {len(conflicts)}")


for conflict in conflicts:

    print("\nTopic:")
    print(conflict.topic)

    print("\nConflicting claims:")

    for claim in conflict.claims:
        print(f"  - {claim}")

    print("\nSources:")

    for source in conflict.sources:
        print(f"  - {source}")