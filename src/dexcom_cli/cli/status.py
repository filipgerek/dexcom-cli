from dexcom_cli.models.region import Region
import typer
from rich.console import Console
from dexcom_cli.auth import Credentials, Session

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def status():
    credentials = Credentials.load()

    if credentials is None:
        console.print(f"[bold orange]Not logged in[/]")
        raise typer.Exit()

    client = Session().create_client()
    account_id = client.get_account_id()
    console.print(f"[bold green]Logged in[/]")
    console.print(f"Username: [bold blue]{credentials.username}[/]")
    console.print(f"Account ID: [bold blue]{account_id}[/]")
    console.print(f"Region: [bold blue]{Region(credentials.region).value.upper()} ({Region(credentials.region).label})[/]")