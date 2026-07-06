import typer
from dexcom_cli.cli.glucose import app as glucose_app
from dexcom_cli.cli.login import app as login_app
from dexcom_cli.cli.logout import app as logout_app

app = typer.Typer()

app.add_typer(glucose_app, name="glucose")
app.add_typer(login_app, name="login")
app.add_typer(logout_app, name="logout")

if __name__ == "__main__":
    app()