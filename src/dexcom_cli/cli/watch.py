import time
import typer
from rich.console import Console
from rich.live import Live
from rich.text import Text

from dexcom_cli.config import DATETIME_FORMAT
from dexcom_cli.services import glucose_service
from dexcom_cli.utils import glucose_color

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def watch():
    try:
        service = glucose_service()
        console.print("[bold yellow]Watching...[/]")
        with Live(Text(""), console=console, refresh_per_second=10) as live:
            while True:
                reading = service.get_current_glucose()
                live.update(Text(f"{reading.value} {reading.unit} {reading.timestamp.strftime(DATETIME_FORMAT)}", style=f"bold {glucose_color(reading.value, reading.unit)}"))
                time.sleep(1)
    except KeyboardInterrupt as e:
        console.print(f"[bold yellow]Stopping...[/]")
        raise typer.Exit(code=0) from e