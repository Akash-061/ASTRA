from app.research.parameters import (
    extract_location,
    extract_research_topic,
    extract_timeframe,
)


text = "research recent issues in Tokyo"

assert (
    extract_timeframe(text)
    == "recent"
)

assert (
    extract_location(text)
    == "Tokyo"
)

assert (
    extract_research_topic(text)
    == "issues"
)


text = "latest AI developments in Japan"

assert (
    extract_timeframe(text)
    == "latest"
)

assert (
    extract_location(text)
    == "Japan"
)

assert (
    extract_research_topic(text)
    == "AI developments"
)


text = "research Python security"

assert (
    extract_location(text)
    is None
)

assert (
    extract_timeframe(text)
    is None
)

assert (
    extract_research_topic(text)
    == "Python security"
)


print("RESEARCH PARAMETERS PASSED")