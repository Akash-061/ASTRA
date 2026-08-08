from rich.console import Console

console = Console()


def show_help():

    console.print("""
[bold cyan]Available Commands[/bold cyan]

cpu
ram
time
help

open calculator
open notepad

exit
""")