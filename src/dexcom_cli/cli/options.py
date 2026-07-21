import typer
from typing import Annotated

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

Simple = Annotated[bool,
    typer.Option(
        "--simple",
        "-s",
        help="Show only glucose measurement and time.",
    )
]
