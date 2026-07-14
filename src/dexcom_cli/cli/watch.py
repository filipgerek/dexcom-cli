import time
import typer
from rich.console import Console
from rich.text import Text

from dexcom_cli.config import DATETIME_FORMAT, REFRESH_INTERVAL
from dexcom_cli.services import glucose_service
from dexcom_cli.utils import glucose_color

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True)
def watch():
    try:
        service = glucose_service()
        console.print("[bold yellow]Watching...[/]")

        last_timestamp = None

        while True:
            reading = service.get_current_glucose()

            if last_timestamp != reading.timestamp:
                console.print(
                    Text(
                        f"{reading.value} {reading.unit} {reading.trend.arrow} {reading.timestamp.strftime(DATETIME_FORMAT)}",
                        style=f"bold {glucose_color(reading.value, reading.unit)}"
                    )
                )
                last_timestamp = reading.timestamp

            time.sleep(REFRESH_INTERVAL)
    except KeyboardInterrupt:
        console.print(f"[bold yellow]Stopping...[/]")
        raise typer.Exit()