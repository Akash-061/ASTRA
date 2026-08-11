from rich.console import Console
from rich.panel import Panel

from app.core.assistant import Assistant
from app.utils.system import get_system_info


console = Console()


def main():

    info = get_system_info()

    console.print(
        Panel.fit(
            "[bold cyan]ASTRA Personal Assistant[/bold cyan]",
            title="🚀 Booting",
        )
    )

    console.print(
        f"[green]Operating System:[/green] "
        f"{info['os']}"
    )

    console.print(
        f"[green]CPU Usage:[/green] "
        f"{info['cpu']}%"
    )

    console.print(
        f"[green]RAM Usage:[/green] "
        f"{info['ram']}%"
    )

    console.print(
        f"[green]Current Time:[/green] "
        f"{info['time']}"
    )

    console.print(
        "\n[bold yellow]"
        "Hello Akash! ASTRA is online."
        "[/bold yellow]"
    )

    assistant = Assistant()

    while True:

        command = input(
            "\nASTRA > "
        ).strip()

        if not command:

            continue

        response = assistant.handle(
            command
        )

        console.print(
            f"\n{response.message}"
        )

        if not response.success:

            console.print(
                "[yellow]The request could "
                "not be completed.[/yellow]"
            )

        if command.lower().strip() in {
            "exit",
            "quit",
            "goodbye",
        }:

            break


if __name__ == "__main__":
    main()