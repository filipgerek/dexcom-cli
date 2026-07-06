import typer
from rich.console import Console

from dexcom_cli.auth import Credentials

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def logout():
    credentials = Credentials.load()
    credentials.delete()
    console.print(f"[bold blue]Successfully logged out[/]")