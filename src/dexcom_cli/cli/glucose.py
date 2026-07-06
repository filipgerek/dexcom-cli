import typer
from rich.console import Console

from dexcom_cli.services.glucose import GlucoseService
from dexcom_cli.utils import glucose_color

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def glucose():
    try:
        service = GlucoseService()
        reading = service.get_current_glucose()
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")
        raise typer.Exit(code=1) from e

    color = glucose_color(reading.value, reading.unit)
    
    console.print(f"[bold {color}]{reading.value} {reading.unit}[/]")
    console.print(f"Updated at: {reading.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")