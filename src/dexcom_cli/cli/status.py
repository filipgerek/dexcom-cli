import typer
from rich.console import Console

from dexcom_cli.auth import Credentials
from dexcom_cli.services import glucose_service
from dexcom_cli.utils import parse_region

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def status():
    credentials = Credentials.load()
    service = glucose_service()
    account_id = service.get_account_id()
    region = parse_region(credentials.region)
    if credentials:
        console.print(f"[bold green]Logged in[/]")
        console.print(f"Username: [bold blue]{credentials.username}[/]")
        console.print(f"Account ID: [bold blue]{account_id}[/]")
        console.print(f"Region: [bold blue]{region}[/]")
    else:
        console.print(f"[bold orange]Not logged in[/]")