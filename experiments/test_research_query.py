from app.research.request import ResearchRequest
from app.research.query import build_research_query


request = ResearchRequest(
    topic="issues",
    location="Chennai",
    timeframe="recent",
)


query = build_research_query(
    request
)


assert (
    query
    == "recent issues in Chennai"
)


request = ResearchRequest(
    topic="AI developments",
    location="Japan",
    timeframe="latest",
)


query = build_research_query(
    request
)


assert (
    query
    == "latest AI developments in Japan"
)


request = ResearchRequest(
    topic="Python security",
)


query = build_research_query(
    request
)


assert (
    query
    == "Python security"
)


print("RESEARCH QUERY PASSED")