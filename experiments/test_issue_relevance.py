from app.research.models import Claim

from app.research.issue_relevance import (
    calculate_category_scores,
    calculate_issue_relevance,
    is_issue,
)


claims = [
    Claim(
        statement="Recurring power outages have affected residents in Adyar.",
        source_title="Chennai power outages continue to affect residents",
        source_url="https://example.com/cities/chennai/power",
    ),
    Claim(
        statement="Street name boards were damaged in Kodungaiyur and residents requested repairs.",
        source_title="Kodungaiyur civic issues need attention",
        source_url="https://example.com/cities/chennai/kodungaiyur",
    ),
    Claim(
        statement="Parking shortages and traffic congestion are affecting Anna Nagar residents.",
        source_title="Anna Nagar faces civic strain",
        source_url="https://example.com/cities/chennai/anna-nagar",
    ),
    Claim(
        statement="Actor-politician Vijay addressed concerns about recent problems surrounding him.",
        source_title="Vijay addresses concerns about recent problems",
        source_url="https://example.com/movies/vijay",
    ),
    Claim(
        statement="Relatives admitted Bharathiraja to a private hospital in Chennai.",
        source_title="Medical bulletin on Bharathiraja's health",
        source_url="https://example.com/cinema/health",
    ),
    Claim(
        statement="A school shooting occurred in Thailand.",
        source_title="Thailand school shooting",
        source_url="https://example.com/thailand/news",
    ),
]


print("Total claims:", len(claims))


for index, claim in enumerate(claims, start=1):

    scores = calculate_category_scores(claim)

    issue_score = calculate_issue_relevance(claim)

    issue = is_issue(claim)

    best_category = max(
        scores,
        key=scores.get,
    )

    print(
        "Claim",
        index,
        "| Category:",
        best_category,
        "| Score:",
        f"{issue_score:.3f}",
        "| Is issue:",
        issue,
        "|",
        claim.statement,
    )