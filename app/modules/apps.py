import os

from rich.console import Console

from app.utils.app_discovery import discover_apps


console = Console()

APPS = discover_apps()


def open_application(command: str):

    app = command.lower().strip()

    for word in ["open", "launch", "start", "run"]:

        if app.startswith(word + " "):
            app = app[len(word):].strip()
            break

    matches = []

    for app_name in APPS:

        if app in app_name:
            matches.append(app_name)

    if len(matches) == 0:

        message = (
            f"Unknown application: {app}"
        )

        console.print(
            f"[red]{message}[/red]"
        )

        return {
            "success": False,
            "message": message,
        }

    elif len(matches) == 1:

        selected_app = matches[0]

    else:

        console.print(
            "[yellow]I found multiple "
            "applications:[/yellow]\n"
        )

        for index, match in enumerate(
            matches,
            start=1,
        ):

            console.print(
                f"{index}. {match.title()}"
            )

        try:

            choice = int(
                input(
                    "\nChoose an application: "
                )
            )

            selected_app = matches[
                choice - 1
            ]

        except (
            ValueError,
            IndexError,
        ):

            message = (
                "Invalid application selection."
            )

            console.print(
                f"[red]{message}[/red]"
            )

            return {
                "success": False,
                "message": message,
            }

    shortcut = APPS[selected_app]

    try:

        os.startfile(
            str(shortcut)
        )

    except Exception as error:

        message = (
            f"Failed to open "
            f"{selected_app.title()}: {error}"
        )

        console.print(
            f"[red]{message}[/red]"
        )

        return {
            "success": False,
            "message": message,
        }

    message = (
        f"Opening {selected_app.title()}..."
    )

    console.print(
        f"[green]{message}[/green]"
    )

    return {
        "success": True,
        "message": message,
        "application": selected_app,
    }