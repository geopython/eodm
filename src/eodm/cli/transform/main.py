import typer

from .apps.metadata import app as metadata

app = typer.Typer(
    name="transform",
    no_args_is_help=True,
    help="Commands for data and metadata transformations",
)

app.add_typer(metadata, name="metadata", help="Commands for metadata transformations")
