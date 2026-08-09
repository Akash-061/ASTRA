from app.research.models import (
    Claim,
    EvidenceGroup,
)


claim_1 = Claim(
    statement="Chennai drainage gaps were reduced.",
    sources=[
        "https://www.thehindu.com/article1"
    ],
)

claim_2 = Claim(
    statement="Stormwater drainage gaps in Chennai have decreased.",
    sources=[
        "https://www.newindianexpress.com/article2"
    ],
)


group = EvidenceGroup(
    representative_claim=claim_1.statement,
    claims=[
        claim_1,
        claim_2,
    ],
    sources=[
        "https://www.thehindu.com/article1",
        "https://www.newindianexpress.com/article2",
    ],
    domains=[
        "thehindu.com",
        "newindianexpress.com",
    ],
    confidence=0.65,
)


print("Representative claim:")
print(group.representative_claim)

print("\nClaims:")
for claim in group.claims:
    print(f"- {claim.statement}")

print("\nSources:")
for source in group.sources:
    print(f"- {source}")

print("\nDomains:")
for domain in group.domains:
    print(f"- {domain}")
print(f"\nConfidence: {group.confidence:.0%}")