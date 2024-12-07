from typing import Iterator

import pystac_client
from pystac import Collection, Item


def extract_stac_api_items(
    url: str,
    collections: list[str] | None = None,
    bbox: tuple[float, float, float, float] | None = None,
    datetime_interval: str | None = None,
    limit: int | None = None,
    query: dict | None = None,
    filter: dict | None = None,
) -> Iterator[Item]:
    """Extracts items from a STAC API

    Args:
        url (str): Link to STAC API endpoint
        collections (list[str] | None, optional): List of collections to extract items from. Defaults to None.
        bbox (tuple[float, float, float, float] | None, optional): Bounding box to search. Defaults to None.
        datetime_interval (str | None, optional): Datetime interval to search. Defaults to None.
        limit (int, optional): Limit query to given number. Defaults to 10.
        query (optional): STACAPI Query extension
        filter (optional): STACAPI CQL Filter extension

    Yields:
        Iterator[Item]: pystac Items
    """

    client = pystac_client.Client.open(url)

    search = client.search(
        collections=collections,
        bbox=bbox,
        datetime=datetime_interval,
        limit=limit,
        query=query,
        filter=filter,
    )

    yield from search.item_collection()


def extract_stac_api_collections(url: str) -> Iterator[Collection]:
    """Extracts collections from a STAC API

    Args:
        url (str): Link to STAC API endpoint

    Yields:
        Iterator[Collection]: pystac Collections
    """

    client = pystac_client.Client.open(url)
    yield from client.get_collections()
