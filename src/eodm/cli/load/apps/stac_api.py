import json
import sys
from typing import Annotated

import httpx
import pystac
import typer

from ....types import DEFAULT_EXTENT

app = typer.Typer(no_args_is_help=True)

HEADERS = {"Content-Type": "application/json"}


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
        collections_endpoint, json=collection.to_dict(), headers=HEADERS, verify=verify
    )

    if update and response.status_code == 409:
        collection_endpoint = f"{collections_endpoint}/{collection.id}"
        response = httpx.put(
            collection_endpoint, json=collection.to_dict(), headers=HEADERS, verify=verify
        )

    response.raise_for_status()


@app.command(no_args_is_help=True)
def collections(
    url: str,
    collections: Annotated[typer.FileText, typer.Argument()] = sys.stdout,  # type: ignore
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
) -> None:
    """
    Load multiple collections to a stac API
    """

    collections_endpoint = f"{url}/collections"
    for line in collections.readlines():
        collection_dict = json.loads(line)
        response = httpx.post(
            collections_endpoint, json=collection_dict, headers=HEADERS, verify=verify
        )
        if response.status_code == 409:
            if update:
                collection_endpoint = f"{collections_endpoint}/{collection_dict['id']}"
                response = httpx.put(
                    collection_endpoint,
                    json=collection_dict,
                    headers=HEADERS,
                    verify=verify,
                )
            if skip_existing:
                continue

        response.raise_for_status()


@app.command(no_args_is_help=True)
def items(
    url: str,
    items: Annotated[typer.FileText, typer.Argument()] = sys.stdin,  # type: ignore
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
) -> None:
    """
    Load multiple items into a STAC API
    """

    for line in items.readlines():
        item_dict = json.loads(line)
        collection_id = item_dict["collection"]
        items_endpoint = f"{url}/collections/{collection_id}/items"
        response = httpx.post(
            items_endpoint, json=item_dict, headers=HEADERS, verify=verify
        )
        if response.status_code == 409:
            if update:
                item_endpoint = f"{items_endpoint}/{item_dict['id']}"
                response = httpx.put(
                    item_endpoint, json=item_dict, headers=HEADERS, verify=verify
                )
            if skip_existing:
                continue
        response.raise_for_status()
