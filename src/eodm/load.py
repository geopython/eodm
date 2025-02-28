from typing import Iterable, Optional, Tuple, Dict

import httpx
from pystac import Collection, Item

DEFAULT_HEADERS = {"Content-Type": "application/json"}


def load_stac_api_items(
    url: str,
    items: Iterable[Item],
    headers: Optional[Dict[str, str]] = None,
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
    auth: Optional[Tuple[str, str]] = None,
) -> Iterable[Item]:
    """Load multiple items into a STAC API

    Args:
        url (str): STAC API url
        items (Iterable[Item]): A collection of STAC Items
        headers (Optional[Dict[str, str]], optional): Headers to add to the request. Defaults to None.
        verify (bool, optional): Verify SSL request. Defaults to True.
        update (bool, optional): Update STAC Item with new content. Defaults to False.
        skip_existing (bool, optional): Skip Item if exists. Defaults to False.
        auth (Optional[Tuple[str, str]], optional): Basic authentication (username, password). Defaults to None.
    """
    if not headers:
        headers = DEFAULT_HEADERS

    with httpx.Client(headers=headers, verify=verify, auth=auth) as client:
        for item in items:
            collection_id = item.collection_id
            items_endpoint = f"{url}/collections/{collection_id}/items"
            response = client.post(
                items_endpoint,
                json=item.to_dict(),
            )
            if response.status_code == 409:
                if update:
                    item_endpoint = f"{items_endpoint}/{item.id}"
                    response = client.put(
                        item_endpoint,
                        json=item.to_dict(),
                    )
                if skip_existing:
                    continue
            response.raise_for_status()
            yield item


def load_stac_api_collections(
    url: str,
    collections: Iterable[Collection],
    headers: Optional[Dict[str, str]] = None,
    verify: bool = True,
    update: bool = False,
    skip_existing: bool = False,
    auth: Optional[Tuple[str, str]] = None,
) -> Iterable[Collection]:
    """Load multiple collections to a stac API

    Args:
        url (str): STAC API URL
        collections (Iterable[Collection]): A collection of STAC Collections
        headers (Optional[Dict[str, str]], optional): Additional headers to send. Defaults to None.
        verify (bool, optional): Verify TLS request. Defaults to True.
        update (bool, optional): Update the destination Collections. Defaults to False.
        skip_existing (bool, optional): Skip existing Collections. Defaults to False.
        auth (Optional[Tuple[str, str]], optional): Basic authentication (username, password). Defaults to None.

    Returns:
        Iterable[Collection]:
    """

    if not headers:
        headers = DEFAULT_HEADERS

    with httpx.Client(headers=headers, verify=verify, auth=auth) as client:
        collections_endpoint = f"{url}/collections"
        for collection in collections:
            response = client.post(
                collections_endpoint,
                json=collection.to_dict(),
            )
            if response.status_code == 409:
                if update:
                    collection_endpoint = f"{collections_endpoint}/{collection.id}"
                    response = client.put(
                        collection_endpoint,
                        json=collection.to_dict(),
                    )
                if skip_existing:
                    continue

            response.raise_for_status()
            yield collection
