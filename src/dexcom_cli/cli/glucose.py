import typer
from rich.console import Console

from dexcom_cli.services.glucose import GlucoseService

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def glucose():
    service = GlucoseService()

    reading = service.get_current_glucose()
    
    console.print(f"[bold green]{reading.value} {reading.unit}")
    console.print(f"Updated at: {reading.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")