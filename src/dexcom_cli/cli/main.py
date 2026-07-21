import typer
from dexcom_cli.cli.chart import app as chart_app
from dexcom_cli.cli.glucose import app as glucose_app
from dexcom_cli.cli.login import app as login_app
from dexcom_cli.cli.logout import app as logout_app
from dexcom_cli.cli.status import app as status_app
from dexcom_cli.cli.history import app as history_app
from dexcom_cli.cli.watch import app as watch_app
app = typer.Typer()

app.add_typer(glucose_app, name="glucose")
app.add_typer(login_app, name="login")
app.add_typer(logout_app, name="logout")
app.add_typer(status_app, name="status")
app.add_typer(history_app, name="history")
app.add_typer(watch_app, name="watch")
app.add_typer(chart_app, name="chart")

if __name__ == "__main__":
    app()
