import typer

app = typer.Typer()

@app.command()
def list(type: str):
    typer.echo(f"List all {type}")

@app.command()
def pull(type: str, name: str):
    typer.echo(f"Downloading {name}")

@app.command()
def status():
    typer.echo(f"Show local status")

if __name__ == "__main__":
    app() 
