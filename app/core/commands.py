import subprocess

from rich.console import Console
from app.utils.system import get_system_info
from app.utils.config import load_apps

console = Console()

APPS = load_apps()

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

        words = command.split()

        if len(words) < 2:
            console.print("[red]Usage:[/red] open <application>")
            return True

        app = words[1]


    if app in APPS:

        subprocess.Popen(APPS[app])

        console.print(f"[green]Opening {app.title()}...[/green]")

    else:

        console.print(f"[red]Unknown application:[/red] {app}")