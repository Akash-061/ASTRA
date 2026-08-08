from rich.console import Console

from app.utils.system import get_system_info

console = Console()


def handle_system_command(command: str):

    command = command.lower().strip()

    info = get_system_info()

    if command == "cpu":

        console.print(f"[green]CPU Usage:[/green] {info['cpu']}%")

    elif command == "ram":

        console.print(f"[green]RAM Usage:[/green] {info['ram']}%")

    elif command == "time":

        console.print(f"[green]Current Time:[/green] {info['time']}")