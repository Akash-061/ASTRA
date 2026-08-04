command = input("Command: ")

words = command.split()

if words[0] == "open":
    print("Opening", words[1])