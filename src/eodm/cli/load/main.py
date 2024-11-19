import typer

from .apps.stac_api import app as stac_api
from .apps.stac_catalog import app as stac_catalog

app = typer.Typer(
    name="load",
    no_args_is_help=True,
    help="Commands for loading data into various destinations",
)
app.add_typer(stac_api, name="stac-api")
app.add_typer(stac_catalog, name="stac-catalog")
