"""Command-line interface for shared_expense_splitter."""

import typer

from shared_expense_splitter import __version__

app = typer.Typer(help="Splits shared expenses among groups.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        callback=_version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
) -> None:
    """shared-expense-splitter CLI."""


if __name__ == "__main__":
    app()
