import typer
from rich.console import Console

from dexcom_cli.auth import Credentials
from dexcom_cli.services import GlucoseService

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def status():
    credentials = Credentials.load()

    if credentials is None:
        console.print(f"[bold orange]Not logged in[/]")
        raise typer.Exit()

    service = GlucoseService(credentials)
    account_id = service.get_account_id()
    console.print(f"[bold green]Logged in[/]")
    console.print(f"Username: [bold blue]{service.username}[/]")
    console.print(f"Account ID: [bold blue]{account_id}[/]")
    console.print(f"Region: [bold blue]{service.region}[/]")