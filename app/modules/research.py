from rich.console import Console

from app.research.search import search_web
from app.research.analyzer import extract_claims
from app.research.relevance import is_relevant
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

    console.print(
        f"[dim]Candidate claims: {len(claims)}[/dim]"
    )

    # Step 3: Filter claims by semantic relevance
    relevant_claims = []

    for claim in claims:

        if is_relevant(
            query,
            claim,
        ):
            relevant_claims.append(claim)

    if not relevant_claims:

        console.print(
            "[yellow]No relevant claims found.[/yellow]"
        )

        return

    console.print(
        f"[green]Relevant claims: "
        f"{len(relevant_claims)}[/green]\n"
    )

    # Step 4: Verify and create evidence groups
    evidence_groups = verify_claims(
        relevant_claims
    )

    if not evidence_groups:

        console.print(
            "[yellow]No evidence groups found.[/yellow]"
        )

        return

    console.print(
        "[bold cyan]Research Evidence[/bold cyan]\n"
    )

    for index, group in enumerate(
        evidence_groups,
        start=1,
    ):

        console.print(
            f"[bold]{index}. "
            f"{group.representative_claim}[/bold]"
        )

        console.print(
            f"[yellow]Evidence confidence:[/yellow] "
            f"{group.confidence:.0%}"
        )

        console.print(
            f"[green]Independent domains:[/green] "
            f"{len(group.domains)}"
        )

        console.print(
            f"[green]Related claims:[/green] "
            f"{len(group.claims)}"
        )

        console.print(
            "[cyan]Sources:[/cyan]"
        )

        for source in group.sources:

            console.print(
                f"  • {source}"
            )

        console.print()