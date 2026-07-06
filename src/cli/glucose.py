import typer
from src.services.glucose import GlucoseService

from rich.console import Console

app = typer.Typer()
console = Console()
@app.command()
def glucose():
    service = GlucoseService()

    reading = service.get_current_glucose()
    
    console.print(f"[bold green]: {reading.value} {reading.unit}")
    console.print(f"Updated at: {reading.timestamp}")