import os

from rich.console import Console
from app.utils.app_discovery import discover_apps

console = Console()

APPS = discover_apps()


def open_application(command: str):

    app = command.lower()

    for word in ["open", "launch", "start", "run"]:

        if app.startswith(word + " "):
            app = app.replace(word + " ", "")
            break

    matches = []

    for app_name in APPS:

        if app in app_name:

            matches.append(app_name)

    if len(matches) == 0:

        console.print(f"[red]Unknown application:[/red] {app}")
        return

    elif len(matches) == 1:

        selected_app = matches[0]

    else:

        console.print("[yellow]I found multiple applications:[/yellow]\n")

        for index, match in enumerate(matches, start=1):
            console.print(f"{index}. {match.title()}")

        choice = int(input("\nChoose an application: "))

        selected_app = matches[choice - 1]

    shortcut = APPS[selected_app]

    os.startfile(str(shortcut))

    console.print(f"[green]Opening {selected_app.title()}...[/green]")