from app.core.router import route


while True:

    command = input("ASTRA > ")

    if not route(command):
        break