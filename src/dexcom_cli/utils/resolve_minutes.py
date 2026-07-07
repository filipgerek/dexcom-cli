import typer

DEFAULT_MINUTES = 60

def resolve_minutes(
    minutes: int | None, 
    hours: int | None
    ) -> int:

    if minutes is not None and hours is not None:
        raise typer.BadParameter("Use either --minutes (-m) or --hours (-H), not both.")

    if hours is not None:
        minutes = hours * 60

    elif minutes is None:
        minutes = DEFAULT_MINUTES

    return minutes
