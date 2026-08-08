from app.modules.system import handle_system_command

while True:

    command = input("Command: ")

    handle_system_command(command)