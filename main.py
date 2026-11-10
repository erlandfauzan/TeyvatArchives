import json
from rich.console import Console
from rich.table import Table
from core.validator import TeyvatArchiveValidator

def main():
    console = Console()
    console.print("[bold cyan]====================================================[/bold cyan]")
    console.print("[bold yellow]  Library Catalog Metadata & MARC21/DDC Validator   [/bold yellow]")
    console.print("[bold cyan]====================================================[/bold cyan]\n")

    data_path = "data/mock_teyvat_books.json"
    try:
        with open(data_path, "r") as f:
            records = json.load(f)
    except FileNotFoundError:
        console.print(f"[bold red]Error: Dataset not found at {data_path}[/bold red]")
        return

    validator = TeyvatArchiveValidator()
    results = [validator.validate_single_record(rec) for rec in records]

    table = Table(title="Bibliographic Compliance Audit Report")
    table.add_column("Book ID", style="cyan", no_wrap=True)
    table.add_column("Title & Department", style="white")
    table.add_column("Status", style="bold")
    table.add_column("Audit Error Findings", style="red")

    pass_count = 0
    fail_count = 0

    for res in results:
        if res.is_valid:
            status_str = "[green]PASS[/green]"
            error_msg = "-"
            pass_count += 1
        else:
            status_str = "[red]FAIL[/red]"
            error_msg = "; ".join(res.errors)
            fail_count += 1
            
        table.add_row(res.book_id, res.title, status_str, error_msg)

    console.print(table)
    console.print(f"\n[bold]Audit Summary:[/bold] Total Records: {len(results)} | [green]Passed: {pass_count}[/green] | [red]Failed: {fail_count}[/red]\n")

if __name__ == "__main__":
    main()