from rich.console import Console

from app.core.models import Action
from app.research.adapter import action_to_research_request
from app.research.engine import run_research


console = Console()


def research(
    action: Action,
):

    request = action_to_research_request(
        action
    )

    console.print(
        f"\n[cyan]🔎 Researching:[/cyan] "
        f"{request.original_query}\n"
    )

    result = run_research(
        request
    )

    if not result["success"]:

        console.print(
            f"[yellow]{result['message']}[/yellow]"
        )

        return result

    data = result.get(
        "data",
        {},
    )

    console.print(
        "[green]Research completed.[/green]\n"
    )

    console.print(
        f"[green]Search query:[/green] "
        f"{data.get('query', '')}"
    )

    console.print(
        f"[green]Sources:[/green] "
        f"{data.get('sources', 0)}"
    )

    console.print(
        f"[green]Candidate claims:[/green] "
        f"{data.get('claims', 0)}"
    )

    console.print(
        f"[green]Relevant claims:[/green] "
        f"{data.get('relevant_claims', 0)}"
    )

    console.print(
        f"[green]Evidence groups:[/green] "
        f"{len(data.get('evidence_groups', []))}"
    )

    console.print()

    for index, group in enumerate(
        data.get(
            "evidence_groups",
            [],
        ),
        start=1,
    ):

        console.print(
            f"[bold]{index}. "
            f"{group.representative_claim}[/bold]"
        )

        console.print(
            f"[yellow]Confidence:[/yellow] "
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

    return result


research.accepts_action = True