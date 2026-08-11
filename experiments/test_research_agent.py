import app.modules.research as research_module

from app.core.models import UserRequest
from app.core.orchestrator import Orchestrator


research_module.run_research = lambda request: {
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


orchestrator = Orchestrator()


request = UserRequest(
    text="research recent issues in Tokyo"
)


response = orchestrator.handle(
    request
)


assert response.success is True

assert (
    "Research completed."
    in response.message
)


print()
print("RESEARCH AGENT RESPONSE:")
print(response.message)
print()
print("FULL RESEARCH AGENT PASSED")