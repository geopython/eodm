from typing import Annotated, cast

import typer

from eodm.cli._globals import DEFAULT_BBOX, DEFAULT_DATETIME_INTERVAL
from eodm.cli._serialization import serialize
from eodm.cli._types import (
    BBoxType,
    DateTimeIntervalType,
    Output,
    OutputType,
)
from eodm.extract import extract_stac_api_collections, extract_stac_api_items

app = typer.Typer(no_args_is_help=True, help="Extract data from a STAC API")


@app.command(no_args_is_help=True)
def items(
    url: str,
    collection: str,
    bbox: BBoxType = DEFAULT_BBOX,
    datetime_interval: DateTimeIntervalType = DEFAULT_DATETIME_INTERVAL,
    limit: Annotated[
        int,
        typer.Option(
            "--limit",
            "-l",
            parser=lambda x: x if x else None,
            metavar="INT",
            help="Limit query.",
        ),
    ] = 0,
    output: OutputType = Output.default,
):
    """
    Extract items from a collection found in a STAC API
    """

    _bbox = None
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
        limit=limit,
    )
    serialize(items, output_type=output)


@app.command(no_args_is_help=True)
def collections(url: str, output: OutputType = Output.default):
    """
    Extract all collections from STAC API
    """

    collections = extract_stac_api_collections(url)
    serialize(collections, output_type=output)
