import plotext as plt
import typer
from rich.console import Console

from dexcom_cli.cli import Hours, Minutes
from dexcom_cli.services import glucose_service
from dexcom_cli.utils import resolve_minutes

console = Console()
app = typer.Typer()


@app.callback(invoke_without_command=True, help="Display glucose readings as a terminal chart.")
def chart(
    minutes: Minutes = None,
    hours: Hours = None,
):
    minutes = resolve_minutes(minutes, hours)

    try:
        service = glucose_service()
        readings = service.get_history(minutes)
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")
        raise typer.Exit(code=1) from e

    if not readings:
        console.print("[bold yellow]No glucose readings found.[/]")
        raise typer.Exit()

    x_values = list(range(len(readings)))
    timestamps = [reading.timestamp.strftime("%H:%M") for reading in readings]
    values = [reading.value for reading in readings]
    unit = readings[0].unit

    plt.clear_figure()
    plt.title(f"Glucose readings - last {minutes} minutes")
    plt.xlabel("Time")
    plt.ylabel(unit)
    plt.xticks(x_values, timestamps)
    plt.plot(x_values, values, marker="dot")
    plt.show()
