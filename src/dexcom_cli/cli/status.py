import typer
from rich.console import Console

from dexcom_cli.auth import Credentials
from dexcom_cli.utils import parse_region

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def status():
    credentials = Credentials.load()
    region = parse_region(credentials.region)
    if credentials:
        console.print(f"[bold green]Logged in[/]")
        console.print(f"Username: [bold blue]{credentials.username}[/]")
        console.print(f"Region: [bold blue]{region}[/]")
    else:
        console.print(f"[bold orange]Not logged in[/]")