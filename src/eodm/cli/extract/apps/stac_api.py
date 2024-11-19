import json

import pystac_client
import typer

from ....types import BBoxType, DateTimeIntervalType

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
):
    client = pystac_client.Client.open(url)

    if bbox:
        _bbox = list(bbox)

    dt = None
    if datetime_interval:
        dt = str(datetime_interval)

    search = client.search(collections=[collection], bbox=_bbox, datetime=dt)
    for item in search.item_collection():
        print(json.dumps(item.to_dict()))


@app.command(no_args_is_help=True)
def collections(url: str):
    client = pystac_client.Client.open(url)

    for collection in client.get_collections():
        print(json.dumps(collection.to_dict()))
