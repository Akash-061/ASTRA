from app.core.context import ConversationContext


context = ConversationContext()

context.add_message("Hello ASTRA")
context.add_message("Open Chrome")
context.add_message("Search for MCA courses")

recent = context.get_recent()

assert len(recent) == 3
assert recent[0] == "Hello ASTRA"
assert recent[-1] == "Search for MCA courses"

context.clear()

assert context.get_recent() == []

print("CONTEXT PASSED")