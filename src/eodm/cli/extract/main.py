import typer

from .apps.openeo import app as openeo
from .apps.opensearch import app as opensearch
from .apps.stac_api import app as stac_api
from .apps.stac_catalog import app as stac_catalog

app = typer.Typer(
    name="extract",
    no_args_is_help=True,
    help="Commands for extracting data from various sources",
)
app.add_typer(stac_api, name="stac-api")
app.add_typer(stac_catalog, name="stac-catalog")
app.add_typer(openeo, name="openeo")
app.add_typer(opensearch, name="opensearch")
