from typing import Iterable

import httpx
from pystac import Collection, Item

DEFAULT_HEADERS = {"Content-Type": "application/json"}


def load_stac_api_items(
    url: str,
    items: Iterable[Item],
    headers: dict[str, str] | None = None,
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
) -> Iterable[Item]:
    """Load multiple items into a STAC API

    Args:
        url (str): STAC API url
        items (Iterable[Item]): A collection of STAC Items
        headers (dict[str, str] | None, optional): Headers to add to the request. Defaults to None.
        verify (bool, optional): Verify SSL request. Defaults to True.
        update (bool, optional): Update STAC Item with new content. Defaults to False.
        skip_existing (bool, optional): Skip Item if exists. Defaults to False.
    """
    if not headers:
        headers = DEFAULT_HEADERS

    for item in items:
        collection_id = item.collection_id
        items_endpoint = f"{url}/collections/{collection_id}/items"
        response = httpx.post(
            items_endpoint,
            json=item.to_dict(),
            headers=headers,
            verify=verify,
        )
        if response.status_code == 409:
            if update:
                item_endpoint = f"{items_endpoint}/{item.id}"
                response = httpx.put(
                    item_endpoint, json=item.to_dict(), headers=headers, verify=verify
                )
            if skip_existing:
                continue
        response.raise_for_status()
        yield item


def load_stac_api_collections(
    url: str,
    collections: Iterable[Collection],
    headers: dict[str, str] | None = None,
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
) -> Iterable[Collection]:
    """Load multiple collections to a stac API

    Args:
        url (str): STAC API URL
        collections (Iterable[Collection]): A collection of STAC Collections
        headers (dict[str, str] | None, optional): Additional headers to send. Defaults to None.
        verify (bool, optional): Verify TLS request. Defaults to True.
        update (bool, optional): Update the destination Collections. Defaults to False.
        skip_existing (bool, optional): Skip existing Collections. Defaults to False.

    Returns:
        Iterable[Collection]:
    """

    if not headers:
        headers = DEFAULT_HEADERS

    collections_endpoint = f"{url}/collections"
    for collection in collections:
        response = httpx.post(
            collections_endpoint,
            json=collection.to_dict(),
            headers=headers,
            verify=verify,
        )
        if response.status_code == 409:
            if update:
                collection_endpoint = f"{collections_endpoint}/{collection.id}"
                response = httpx.put(
                    collection_endpoint,
                    json=collection.to_dict(),
                    headers=headers,
                    verify=verify,
                )
            if skip_existing:
                continue

        response.raise_for_status()
        yield collection
