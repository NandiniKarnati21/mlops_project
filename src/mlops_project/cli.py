"""Console script for mlops_project."""

import typer
from rich.console import Console

from mlops_project import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for mlops_project."""
    console.print("Replace this message by putting your code into "
               "mlops_project.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
