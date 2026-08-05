import os

from rich.console import Console

from app.utils.system import get_system_info
from app.utils.app_discovery import discover_apps

console = Console()

APPS = discover_apps()

print(APPS.get("google chrome"))


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

        if app in APPS:

            shortcut = APPS[app]

            os.startfile(str(shortcut))
            
            console.print(f"[green]Opening {app.title()}...[/green]")

        else:

            console.print(f"[red]Unknown application:[/red] {app}")

    return True