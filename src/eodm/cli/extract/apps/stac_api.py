from typing import cast

import typer

from eodm.cli._types import BBoxType, DateTimeIntervalType, Output, OutputType
from eodm.encoder import OUTPUT_ENCODERS
from eodm.extract import extract_stac_api_collections, extract_stac_api_items

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
    output_encoder = OUTPUT_ENCODERS[output]
    output_encoder(items)


@app.command(no_args_is_help=True)
def collections(url: str, output: OutputType = Output.default):
    """
    Extract collections from STAC API
    """

    collections = extract_stac_api_collections(url)

    output_encoder = OUTPUT_ENCODERS[output]
    output_encoder(collections)
