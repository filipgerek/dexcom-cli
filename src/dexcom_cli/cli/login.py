import typer
from rich.console import Console

from dexcom_cli.auth import Credentials
from dexcom_cli.clients import PydexcomClient
console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def login():
    username = typer.prompt("Dexcom username")
    password = typer.prompt("Dexcom password", hide_input=True)
    region = typer.prompt("Dexcom region", default="us", show_default=True)

    credentials = Credentials(username=username, password=password, region=region)

    try:
        client = PydexcomClient(username=username, password=password, region=region)
        _ = client.current_glucose()
    except Exception as e:
        console.print(f"[bold red]Login failed:[/] {e}")
        raise typer.Exit(code=1) from e

    credentials.save()
    console.print(f"[bold green]Successfully logged in as {username}[/]")