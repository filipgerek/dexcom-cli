import typer
from rich.console import Console

from dexcom_cli.services import glucose_service

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def history():
    try:
        service = glucose_service()
        history = service.get_history(minutes=60)
        for reading in history:
            console.print(f"{reading.value} {reading.unit} at {reading.timestamp}")
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")
        raise typer.Exit(code=1) from e
    