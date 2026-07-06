import typer
from dexcom_cli.cli.glucose import glucose

app = typer.Typer()

@app.command()
def glucose():
    glucose()

if __name__ == "__main__":
    app()