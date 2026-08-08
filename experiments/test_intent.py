from app.core.intent import detect_intent

while True:

    command = input("Command: ")

    intent = detect_intent(command)

    print(f"Intent: {intent}")