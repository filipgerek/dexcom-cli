import typer
from dexcom_cli.cli.glucose import app as glucose_app


app = typer.Typer()

app.add_typer(glucose_app, name="glucose")

if __name__ == "__main__":
    app()