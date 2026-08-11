import app.modules.research as research_module

from app.core.models import Action


research_module.run_research = (
    lambda request: {
        "success": True,
        "message": "Research completed.",
        "data": {
            "query": "recent issues in Tokyo",
            "sources": 3,
            "claims": 5,
            "relevant_claims": 3,
            "evidence_groups": [],
        },
    }
)


action = Action(
    name="research",
    parameters={
        "command": (
            "research recent issues in Tokyo"
        ),
        "topic": "issues",
        "location": "Tokyo",
        "timeframe": "recent",
    },
)


result = research_module.research(
    action
)


assert result.success is True

assert (
    result.message
    == "Research completed."
)

assert (
    result.data["query"]
    == "recent issues in Tokyo"
)

assert (
    result.data["sources"]
    == 3
)

assert (
    result.data["claims"]
    == 5
)

assert (
    result.data["relevant_claims"]
    == 3
)

assert (
    result.data["evidence_groups"]
    == []
)


print("RESEARCH MODULE PASSED")