import app.modules.research as research_module

from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


# --------------------------------------------------
# Mock research engine
# --------------------------------------------------

research_module.run_research = (
    lambda request: {
        "success": True,
        "message": "Research completed.",
        "data": {
            "query": "recent issues in Tokyo",
            "sources": 4,
            "claims": 7,
            "relevant_claims": 5,
            "evidence_groups": [],
        },
    }
)


# --------------------------------------------------
# Run through the real orchestrator
# --------------------------------------------------

orchestrator = Orchestrator()

request = UserRequest(
    text="research recent issues in Tokyo"
)

response = orchestrator.handle(
    request
)


# --------------------------------------------------
# Basic response assertions
# --------------------------------------------------

assert response.success is True

assert (
    "Research completed."
    in response.message
)


# --------------------------------------------------
# Verify research data survived
# --------------------------------------------------

assert (
    "query"
    in response.data
)

assert (
    response.data["query"]
    == "recent issues in Tokyo"
)

assert (
    response.data["sources"]
    == 4
)

assert (
    response.data["claims"]
    == 7
)

assert (
    response.data["relevant_claims"]
    == 5
)

assert (
    response.data["evidence_groups"]
    == []
)


# --------------------------------------------------
# Verify orchestrator result collection
# --------------------------------------------------

assert (
    "results"
    in response.data
)

assert (
    len(
        response.data["results"]
    )
    == 1
)

research_result = (
    response.data["results"][0]
)

assert (
    research_result["success"]
    is True
)

assert (
    research_result["message"]
    == "Research completed."
)

assert (
    research_result["data"]["query"]
    == "recent issues in Tokyo"
)

assert (
    research_result["data"]["sources"]
    == 4
)


# --------------------------------------------------
# Output
# --------------------------------------------------

print()
print("RESEARCH AGENT RESPONSE:")
print(response.message)

print()
print("RESEARCH DATA:")
print(response.data)

print()
print("FULL RESEARCH AGENT PASSED")