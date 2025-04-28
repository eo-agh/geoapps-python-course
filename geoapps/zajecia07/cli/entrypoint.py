import typer
from typing import Optional

app = typer.Typer()


@app.command()
def add(a: int, b: int):
    """Dodawanie dwóch liczb."""
    typer.echo(f"Wynik: {a + b}")


@app.command()
def multiply(a: int, b: int):
    """Mnożenie dwóch liczb."""
    typer.echo(f"Wynik: {a * b}")


@app.command()
def greet(name: Optional[str] = typer.Argument(None, help="Twoje imię")):
    """
    Powitanie i nic więcej.
    """
    if name:
        typer.echo(f"Witaj {name}!")
        typer.echo("Dzisiaj jest świetny dzień na kodowanie!")
    else:
        typer.echo("Witaj nieznajomy!")
        typer.echo("Dzisiaj jest świetny dzień na kodowanie!")


if __name__ == "__main__":
    app()
