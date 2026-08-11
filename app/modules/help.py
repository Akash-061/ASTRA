from rich.console import Console


console = Console()


HELP_TEXT = """
[bold cyan]Available Commands[/bold cyan]

cpu
ram
time
help

open calculator
open notepad

exit
"""


def show_help():

    console.print(HELP_TEXT)

    return {
        "success": True,
        "message": (
            "Here are the commands I currently support:\n"
            "cpu\n"
            "ram\n"
            "time\n"
            "help\n"
            "open calculator\n"
            "open notepad\n"
            "exit"
        ),
    }