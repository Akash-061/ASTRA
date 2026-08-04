from rich.console import Console
from rich.panel import Panel

from app.utils.system import get_system_info
from app.core.commands import execute_command

console = Console()


def main():
    info = get_system_info()

    console.print(
        Panel.fit(
            "[bold cyan]ASTRA Personal Assistant[/bold cyan]",
            title="🚀 Booting",
        )
    )

    console.print(f"[green]Operating System:[/green] {info['os']}")
    console.print(f"[green]CPU Usage:[/green] {info['cpu']}%")
    console.print(f"[green]RAM Usage:[/green] {info['ram']}%")
    console.print(f"[green]Current Time:[/green] {info['time']}")
    console.print("\n[bold yellow]Hello Akash! ASTRA is online.[/bold yellow]")

    while True:
        command = input("\nASTRA > ")

        if not execute_command(command):
            break


if __name__ == "__main__":
    main()