import importlib
import importlib.metadata
import sys

import typer
from dotenv import load_dotenv

from .cli.extract import app as extract
from .cli.load import app as load
from .cli.transform import app as transform

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points

discovered_plugins = entry_points(group="eodm.plugins")
CLI_NAME = "eodm"

app = typer.Typer(name=CLI_NAME, no_args_is_help=True)

try:
    extract_plugins = discovered_plugins["extract"].load()
    extract.add_typer(extract_plugins)
except KeyError:
    pass
app.add_typer(extract)

try:
    transform_plugins = discovered_plugins["transform"].load()
    transform.add_typer(transform_plugins)
except KeyError:
    pass
app.add_typer(transform)

try:
    load_plugins = discovered_plugins["load"].load()
    load.add_typer(load_plugins)
except KeyError:
    pass
app.add_typer(load)


@app.callback()
def main(with_env: bool = False):
    """
    Create batch ETL of Earth Observation data for various sources and targets.
    """
    if with_env:
        load_dotenv()


@app.command()
def version():
    """
    Prints software version
    """
    version = version = importlib.metadata.version("eodm")
    print(version)


if __name__ == "__main__":
    app()
