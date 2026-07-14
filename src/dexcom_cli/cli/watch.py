import time
import typer
from rich.console import Console
from rich.live import Live
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

        with Live(Text(""), console=console, refresh_per_second=10) as live:
            while True:
                reading = service.get_current_glucose()

                output = (
                    f"{reading.value} "
                    f"{reading.unit} "
                    f"{reading.trend.arrow} "
                    f"{reading.timestamp.strftime(DATETIME_FORMAT)}"
                )

                if last_timestamp != reading.timestamp:
                    live.update(Text(output, style=f"bold {glucose_color(reading.value, reading.unit)}"))
                    last_timestamp = reading.timestamp

                time.sleep(REFRESH_INTERVAL)

    except KeyboardInterrupt:
        console.print(f"[bold yellow]Stopping...[/]")
        raise typer.Exit()