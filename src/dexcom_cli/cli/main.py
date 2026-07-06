import typer
from dexcom_cli.cli.glucose import app as glucose_app
from dexcom_cli.cli.login import app as login_app


app = typer.Typer()

app.add_typer(glucose_app, name="glucose")
app.add_typer(login_app, name="login")

if __name__ == "__main__":
    app()