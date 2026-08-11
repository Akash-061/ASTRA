from rich.console import Console

from app.utils.system import get_system_info


console = Console()


def handle_system_command(command: str):

    command = command.lower().strip()

    info = get_system_info()

    if command == "cpu":

        message = (
            f"CPU Usage: {info['cpu']}%"
        )

        console.print(
            f"[green]{message}[/green]"
        )

        return {
            "success": True,
            "message": message,
            "data": {
                "cpu": info["cpu"],
            },
        }

    elif command == "ram":

        message = (
            f"RAM Usage: {info['ram']}%"
        )

        console.print(
            f"[green]{message}[/green]"
        )

        return {
            "success": True,
            "message": message,
            "data": {
                "ram": info["ram"],
            },
        }

    elif command == "time":

        message = (
            f"Current Time: {info['time']}"
        )

        console.print(
            f"[green]{message}[/green]"
        )

        return {
            "success": True,
            "message": message,
            "data": {
                "time": info["time"],
            },
        }

    message = (
        f"Unknown system command: {command}"
    )

    console.print(
        f"[red]{message}[/red]"
    )

    return {
        "success": False,
        "message": message,
    }