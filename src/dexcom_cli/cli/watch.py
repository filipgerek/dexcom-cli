import time
import typer
from rich.console import Console
from rich.text import Text

from dexcom_cli.config import DATETIME_FORMAT, REFRESH_INTERVAL
from dexcom_cli.services import glucose_service
from dexcom_cli.utils import glucose_color
from dexcom_cli.notifications import play
from dexcom_cli.utils import resolve_sound
from dexcom_cli.cli import Simple

console = Console()
app = typer.Typer()

@app.callback(invoke_without_command=True, help="Watch function for glucose readings updated every 5 minutes, plays a sound when the glucose reading hits a threshold (hypo or hyper).")
def watch(
    simple: Simple = False,
):
    try:
        service = glucose_service()
        console.print("[bold yellow]Watching...[/]")

        last_timestamp = None

        while True:
            reading = service.get_current_glucose()

            if last_timestamp != reading.timestamp:
                reading_text = (
                    f"{reading.value} {reading.unit} {reading.timestamp.strftime('%H:%M')}"
                    if simple
                    else f"{reading.value} {reading.unit} {reading.trend.arrow} {reading.timestamp.strftime(DATETIME_FORMAT)}"
                )

                console.print(
                    Text(
                        reading_text,
                        style=f"bold {glucose_color(reading.value, reading.unit)}"
                    )
                )
                last_timestamp = reading.timestamp

                # Play sound logic
                sound = resolve_sound(reading)
                if sound:
                    play(sound)

            time.sleep(REFRESH_INTERVAL)
    except KeyboardInterrupt:
        console.print("[bold yellow]Stopping...[/]")
        raise typer.Exit()
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")
        raise typer.Exit() from e
