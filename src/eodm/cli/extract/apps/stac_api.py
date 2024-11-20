from typing import cast

import typer

from eodm.cli._types import BBoxType, DateTimeIntervalType, Output, OutputType
from eodm.extract import extract_stac_api_collections, extract_stac_api_items
from eodm.serialize import serialize

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main():
    """
    Extract data from a STAC API
    """


@app.command(no_args_is_help=True)
def items(
    url: str,
    collection: str,
    bbox: BBoxType = None,
    datetime_interval: DateTimeIntervalType = None,
    output: OutputType = Output.default,
):
    """
    Extract items from STAC API
    """
    if bbox:
        _bbox = cast(tuple[float, float, float, float], tuple(bbox))

    dt = None
    if datetime_interval:
        dt = str(datetime_interval)

    items = extract_stac_api_items(
        url=url,
        collections=[collection],
        bbox=_bbox,
        datetime_interval=dt,
    )
    serialize(items, output_type=output)


@app.command(no_args_is_help=True)
def collections(url: str, output: OutputType = Output.default):
    """
    Extract collections from STAC API
    """

    collections = extract_stac_api_collections(url)
    serialize(collections, output_type=output)
