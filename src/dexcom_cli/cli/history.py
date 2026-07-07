import typer
from rich.console import Console
from typing import Annotated

from dexcom_cli.services import glucose_service

console = Console()
app = typer.Typer()

DEFAULT_MINUTES = 60
MIN_MINUTES = 1
MAX_MINUTES = 1440

Minutes = Annotated[int, typer.Option(
    "--minutes", 
    "-m", 
    help="Number of minutes to get history for", 
    min=MIN_MINUTES, 
    max=MAX_MINUTES, 
    show_default=True
)]

@app.callback(invoke_without_command=True)
def history(
    minutes: Minutes = DEFAULT_MINUTES,
):
    try:
        service = glucose_service()
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")
        raise typer.Exit(code=1) from e
    
    history = service.get_history(minutes=minutes)
    for reading in history:
        console.print(f"{reading.value} {reading.unit} at {reading.timestamp}")
    