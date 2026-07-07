import typer
from rich.console import Console
from typing import Annotated

from dexcom_cli.config import DATETIME_FORMAT
from dexcom_cli.services import glucose_service
from dexcom_cli.utils import resolve_minutes

console = Console()
app = typer.Typer()

MIN_MINUTES = 1
MAX_MINUTES = 1440

MIN_HOURS = 1
MAX_HOURS = 24

Minutes = Annotated[int | None, 
    typer.Option(
        "--minutes", 
        "-m", 
        help="Number of minutes to get history for", 
        min=MIN_MINUTES, 
        max=MAX_MINUTES, 
        show_default=True
    )
]

Hours = Annotated[int | None, 
    typer.Option(
        "--hours", 
        "-H", 
        help="Number of hours to get history for", 
        min=MIN_HOURS, 
        max=MAX_HOURS, 
        show_default=True
    )
]

@app.callback(invoke_without_command=True)
def history(
    minutes: Minutes = None,
    hours: Hours = None,
):
    try:
        service = glucose_service()
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")
        raise typer.Exit(code=1) from e
    
    minutes = resolve_minutes(minutes, hours)

    readings = service.get_history(minutes)
    
    for reading in readings:
        console.print(f"{reading.value} {reading.unit} at {reading.timestamp.strftime(DATETIME_FORMAT)}")
    