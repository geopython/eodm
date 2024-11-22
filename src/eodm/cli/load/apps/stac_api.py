import json
import sys
from typing import Annotated

import httpx
import pystac
import typer

from eodm.cli._globals import DEFAULT_EXTENT
from eodm.cli._serialization import serialize
from eodm.cli._types import Output, OutputType
from eodm.load import load_stac_api_collections, load_stac_api_items

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main():
    """
    Load metadata to a STAC API
    """


@app.command(no_args_is_help=True)
def collection(
    url: str,
    id: str,
    description: str,
    title: str,
    verify: bool = True,
    update: bool = False,
) -> None:
    """
    Create and load a single collection to a STAC API.
    """

    collections_endpoint = f"{url}/collections"

    collection = pystac.Collection(
        id=id, description=description, extent=DEFAULT_EXTENT, title=title
    )

    response = httpx.post(
        collections_endpoint, json=collection.to_dict(), headers={}, verify=verify
    )

    if update and response.status_code == 409:
        collection_endpoint = f"{collections_endpoint}/{collection.id}"
        response = httpx.put(
            collection_endpoint, json=collection.to_dict(), headers={}, verify=verify
        )

    response.raise_for_status()


@app.command(no_args_is_help=True)
def collections(
    url: str,
    collections: Annotated[typer.FileText, typer.Argument()] = sys.stdout,  # type: ignore
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
    output: OutputType = Output.default,
) -> None:
    """
    Load multiple collections to a stac API. Collections can be piped from STDIN or a file
    with Collection jsons on each line
    """

    _collections = [
        pystac.Collection.from_dict(json.loads(line)) for line in collections.readlines()
    ]
    serialize(
        load_stac_api_collections(
            url=url,
            collections=_collections,
            verify=verify,
            update=update,
            skip_existing=skip_existing,
        ),
        output_type=output,
    )


@app.command(no_args_is_help=True)
def items(
    url: str,
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
    output: OutputType = Output.default,
) -> None:
    """
    Load multiple items into a STAC API
    """

    _items = [pystac.Item.from_dict(json.loads(line)) for line in items.readlines()]
    serialize(
        load_stac_api_items(
            url=url,
            items=_items,
            verify=verify,
            update=update,
            skip_existing=skip_existing,
        ),
        output_type=output,
    )
