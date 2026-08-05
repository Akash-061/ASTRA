import os

from rich.console import Console

from app.utils.system import get_system_info
from app.utils.app_discovery import discover_apps

console = Console()

APPS = discover_apps()



def execute_command(command: str) -> bool:
    """
    Returns True if ASTRA should continue running.
    Returns False if ASTRA should exit.
    """
    
    command = command.strip().lower()

    if command == "exit":
        console.print("[red]Goodbye, Akash![/red]")
        return False

    elif command == "cpu":
        info = get_system_info()
        console.print(f"[green]CPU Usage:[/green] {info['cpu']}%")

    elif command == "ram":
        info = get_system_info()
        console.print(f"[green]RAM Usage:[/green] {info['ram']}%")

    elif command == "time":
        info = get_system_info()
        console.print(f"[green]Current Time:[/green] {info['time']}")

    elif command == "help":
        console.print("""
Available Commands
------------------
cpu
ram
time
help
open calculator
open notepad
exit
""")

    elif command.startswith("open "):

        app = command.replace("open ", "").lower()

        matches = []

    # Search for matching applications
    for app_name in APPS:

        if app in app_name:
            matches.append(app_name)

    # No matches
    if len(matches) == 0:

        console.print(f"[red]Unknown application:[/red] {app}")

    # Exactly one match
    elif len(matches) == 1:

        selected_app = matches[0]

        shortcut = APPS[selected_app]

        os.startfile(str(shortcut))

        console.print(f"[green]Opening {selected_app.title()}...[/green]")

    # Multiple matches
    else:

        console.print("[yellow]I found multiple applications:[/yellow]\n")

        for index, match in enumerate(matches, start=1):
            console.print(f"{index}. {match.title()}")

        choice = int(input("\nChoose an application: "))

        selected_app = matches[choice - 1]

        shortcut = APPS[selected_app]

        os.startfile(str(shortcut))

        console.print(f"[green]Opening {selected_app.title()}...[/green]")