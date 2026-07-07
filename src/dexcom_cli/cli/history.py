import typer
from rich.console import Console
from typing import Annotated

from dexcom_cli.config import DATETIME_FORMAT
from dexcom_cli.services import glucose_service
from dexcom_cli.utils import resolve_minutes
from dexcom_cli.cli import Minutes, Hours

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def history(
    minutes: Minutes = None,
    hours: Hours = None,
):
    try:
        service = glucose_service()
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")
        raise typer.Exit(code=1) from e
    
    minutes = resolve_minutes(minutes, hours)

    readings = service.get_history(minutes)

    for reading in readings:
        console.print(f"{reading.value} {reading.unit} at {reading.timestamp.strftime(DATETIME_FORMAT)}")
    