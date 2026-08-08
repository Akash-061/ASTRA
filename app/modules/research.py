from rich.console import Console

from app.research.search import search_web
from app.research.analyzer import extract_claims
from app.research.verifier import verify_claims


console = Console()


def clean_query(command: str) -> str:

    command = command.strip().lower()

    prefixes = [
        "search the web for ",
        "search the web ",
        "search for ",
        "search ",
        "research ",
        "look up ",
        "find out ",
    ]

    for prefix in prefixes:

        if command.startswith(prefix):
            return command[len(prefix):].strip()

    return command


def research(command: str):

    console.print(
        f"\n[cyan]🔎 Researching:[/cyan] {command}\n"
    )

    query = clean_query(command)

    console.print(
        f"[dim]Search query:[/dim] {query}\n"
    )

    # Step 1: Search
    results = search_web(query)

    if not results:

        console.print(
            "[yellow]No results found.[/yellow]"
        )

        return

    console.print(
        f"[green]Found {len(results)} unique sources.[/green]\n"
    )

    # Step 2: Extract candidate claims
    claims = extract_claims(results)

    if not claims:

        console.print(
            "[yellow]No useful claims found.[/yellow]"
        )

        return

    # Step 3: Verify / aggregate claims
    verified_claims = verify_claims(claims)

    console.print(
        "[bold cyan]Research Evidence[/bold cyan]\n"
    )

    for index, claim in enumerate(
        verified_claims,
        start=1
    ):

        console.print(
            f"[bold]{index}. {claim.statement}[/bold]"
        )

        console.print(
            f"[yellow]Evidence confidence:[/yellow] "
            f"{claim.confidence:.0%}"
        )

        console.print(
            f"[green]Independent sources:[/green] "
            f"{len(claim.sources)}"
        )

        for source in claim.sources:

            console.print(
                f"  • {source}"
            )

        console.print()