from app.research.models import Claim


claim = Claim(
    statement="Chennai has reported stormwater drainage issues.",
    sources=[
        "https://example.com/article1",
        "https://example.com/article2",
    ],
    confidence=0.75,
)


print("Statement:")
print(claim.statement)

print("\nSources:")

for source in claim.sources:
    print(source)

print(f"\nConfidence: {claim.confidence}")